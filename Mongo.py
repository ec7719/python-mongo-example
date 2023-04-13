from PIL import Image
import io
import pymongo as pm
# Create a client
client = pm.MongoClient("mongodb://localhost:27017")
print(client)
# Create a database
db=client['NovaData']
collection=db['Noacollection']
with open("luffy/batista.jpeg", "rb") as image_file:
    image_data = image_file.read()
image = Image.open(io.BytesIO(image_data))
dict={'_id':'Mia','name':image_data}
collection.insert_one(dict)