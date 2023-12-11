from google.cloud import firestore

# Initialize Firestore client
db = firestore.Client()

# Data Modeling
# Consider a data structure for flats
flats = [
    {'name': 'Spacious Apartment', 'price': 1500, 'location': 'City Center'},
    {'name': 'Cozy Studio', 'price': 1000, 'location': 'Suburb'},
    # ... more flats
]

# Write data to Firestore
for flat in flats:
    db.collection('flats').add(flat)

# Use Indexes
# Firestore automatically creates indexes for simple queries.

# Limit and Paginate Results
# Limit to the first 5 flats
limited_query = db.collection('flats').limit(5).stream()
print("Limited Results:")
for doc in limited_query:
    print(doc.id, doc.to_dict())

# Paginate results
page_size = 5
start_after_doc = None

while True:
    paginated_query = db.collection('flats').start_after(start_after_doc).limit(page_size).stream()
    for doc in paginated_query:
        print(doc.id, doc.to_dict())
        start_after_doc = doc

    if len(list(paginated_query)) < page_size:
        break

# Avoid Deep Nesting
# Flatten the data structure
flat_data = {
    'flat1': {'name': 'Spacious Apartment', 'price': 1500, 'location': 'City Center'},
    'flat2': {'name': 'Cozy Studio', 'price': 1000, 'location': 'Suburb'},
}

# Selective Retrieval
# Retrieve only the 'name' and 'price' fields
selected_query = db.collection('flats').select(['name', 'price']).stream()
print("Selected Fields:")
for doc in selected_query:
    print(doc.id, doc.to_dict())

# Use Where Clauses
# Retrieve documents with a specific price range
min_price = 1000
max_price = 2000
where_query = db.collection('flats').where('price', '>=', min_price).where('price', '<=', max_price).stream()
print("Filtered Results:")
for doc in where_query:
    print(doc.id, doc.to_dict())

# Optimize for Write Operations
# Batching write operations (multiple writes in a single batch)
batch = db.batch()
batch.set(db.collection('flats').document(), {'name': 'New Flat 1', 'price': 1200, 'location': 'Downtown'})
batch.set(db.collection('flats').document(), {'name': 'New Flat 2', 'price': 1800, 'location': 'Suburb'})
batch.commit()

# Monitor Usage and Costs
# Use Firestore console and monitoring tools for analysis

# Additional: Delete data (clean up after testing)
docs_to_delete = db.collection('flats').limit(10).stream()
for doc in docs_to_delete:
    doc.reference.delete()
