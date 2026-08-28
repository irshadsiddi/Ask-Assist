from typing import Optional
from datetime import datetime,date

from sqlmodel import SQLModel, Field, Column
from sqlalchemy import JSON as SAJSON



# USER MODEL
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = None 
    email: str
    role: str = "student"
    created_at: datetime = Field(default_factory=datetime.utcnow)


# FACULTY MODEL
class Faculty(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    department : str
    office_location: str
    email: str
    phone: Optional[str] = None


# ============================================================================
# CANTEEN MODEL
# ============================================================================

class Canteen(SQLModel, table=True):
    """
    Canteen table for campus food outlets
    
    Attributes:
        id: Unique identifier
        name: Canteen name (e.g., "Roy Canteen")
        phone: Contact phone number
        email: Contact email
        location: Physical location description
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str  # Required - canteen must have a name
    phone: str  # Contact for orders/queries
    email: Optional[str] = None  # Contact email
    location: Optional[str] = None  # Where it's located on campus

# ============================================================================
# WARDEN MODEL
# ============================================================================

class Warden(SQLModel, table=True):
    """
    Warden table for hostel warden information
    
    Attributes:
        id: Unique identifier
        name: Warden's full name
        hall: Hostel hall name/number
        phone: Contact phone number
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str  # Required - warden's name
    hall: Optional[str] = None  # Which hostel they manage
    phone: Optional[str] = None  # Emergency contact number

# ============================================================================
# BUILDING MODEL
# ============================================================================

class Building(SQLModel, table=True):
    """
    Building table for campus building information
    
    Attributes:
        id: Unique identifier
        name: Full building name (e.g., "Academic Block A")
        code: Short code (e.g., "AB")
        address: Physical address description
        lat: Latitude coordinate for maps
        lng: Longitude coordinate for maps
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str  # Required - building name
    code: Optional[str] = None  # Short abbreviation for quick reference
    address: Optional[str] = None  # Detailed location
    lat: Optional[float] = None  # GPS latitude
    lng: Optional[float] = None  # GPS longitude

# ============================================================================
# ROOM MODEL
# ============================================================================

class Room(SQLModel, table=True):
    """
    Room table for individual rooms within buildings
    
    Attributes:
        id: Unique identifier
        room_no: Room number (e.g., "AB-201")
        building: Building name
        floor: Floor number
        map_link: URL to Google Maps or campus map
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    room_no: str  # Unique room identifier
    building: Optional[str] = None  # Building name
    floor: Optional[str] = None  # Floor number
    map_link: str  # Navigation link

# ============================================================================
# DOCUMENT MODEL
# ============================================================================

class Document(SQLModel, table=True):
    """
    Document table for storing uploaded files and PDFs
    
    Attributes:
        id: Unique identifier
        title: Document title/name
        department: Which department uploaded it
        storage_path: File path or cloud storage URL
        extracted_text: Text content extracted from PDF (for search)
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    title: Optional[str] = None  # Document name
    department: Optional[str] = None  # Source department
    storage_path: Optional[str] = None  # Where file is stored
    extracted_text: Optional[str] = None  # OCR/parsed text content

# ============================================================================
# NOTICE MODEL
# ============================================================================

class Notice(SQLModel, table=True):
    """
    Notice table for campus announcements and notifications
    
    Attributes:
        id: Unique identifier
        doc_id: Foreign key linking to Document table
        title: Notice headline
        summary: Brief description
        published_date: When notice was posted
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    doc_id: Optional[int] = None  # Links to Document.id
    title: Optional[str] = None  # Notice title
    summary: Optional[str] = None  # Short description
    published_date: Optional[date] = None  # Publication date

# ============================================================================
# EMBEDDING MODEL
# ============================================================================

class Embedding(SQLModel, table=True):
    id: Optional[int] = Field(default=None , primary_key=True)
    doc_id: Optional[int] = None
    chunk_index: int=0
    text_chunk: Optional[str]=None
    embedding: Optional[list]= Field(default=None, sa_column=Column(SAJSON))
    created_at: datetime = Field(default_factory=datetime.utcnow)
