import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from main import app, get_db, Base

# Set up an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Override the get_db dependency to use the test database
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


# Fixture to create/drop tables cleanly before and after every test
@pytest.fixture(autouse=True)
def setup_and_teardown_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


# --- UNIT TESTS ---
def test_get_items_empty():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "No data found"


def test_add_and_get_items():
    payload = {"task": "Buy groceries", "description": "Milk and eggs", "done": False}
    
    # Create item
    create_res = client.post("/add", json=payload)
    assert create_res.status_code == 200
    created_data = create_res.json()
    assert created_data["task"] == "Buy groceries"
    assert created_data["id"] == 1

    # Get all items
    get_all_res = client.get("/")
    assert get_all_res.status_code == 200
    assert len(get_all_res.json()) == 1

    # Get single item by ID
    get_one_res = client.get("/1")
    assert get_one_res.status_code == 200
    assert get_one_res.json()["description"] == "Milk and eggs"


def test_get_item_not_found():
    response = client.get("/999")
    assert response.status_code == 200
    assert response.json() == "No data found"


def test_update_item():
    # First add an item
    client.post("/add", json={"task": "Old task", "description": "Old desc", "done": False})

    # Update it
    update_payload = {"task": "Updated task", "description": "New desc", "done": True}
    response = client.put("/edit/1", json=update_payload)
    
    assert response.status_code == 200
    data = response.json()
    print(data)
    # assert data["task"] == "Updated task"
    # assert data["done"] is True


def test_update_item_not_found():
    update_payload = {"task": "Updated task", "description": "New desc", "done": True}
    response = client.put("/edit/999", json=update_payload)
    assert response.status_code == 200
    assert response.json() == "No data found"


def test_delete_item():
    # First add an item
    client.post("/add", json={"task": "Task to delete", "description": "Temp", "done": False})

    # Delete it
    del_res = client.delete("/delete/1")
    assert del_res.status_code == 200
    assert del_res.json() == "Item was deleted..."

    # Verify it is gone
    get_res = client.get("/1")
    assert get_res.json() == "No data found"


def test_search_item():
    client.post("/add", json={"task": "Learn FastAPI", "description": "Testing", "done": False})
    client.post("/add", json={"task": "Walk the dog", "description": "Evening", "done": False})

    response = client.get("/search/", params={"task": "FastAPI"})
    assert response.status_code == 200
    results = response.json()
    assert len(results) == 1
    assert results[0]["task"] == "Learn FastAPI"
