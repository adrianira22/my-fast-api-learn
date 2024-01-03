from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

# PENJELASAN

# from fastapi import FastAPI: Baris ini mengimpor kelas FastAPI dari modul fastapi. FastAPI adalah kelas utama yang memungkinkan kita membuat dan menentukan rute API.

# app = FastAPI(): Baris ini membuat instance kelas FastAPI dan menugaskannya ke variabel app. Objek aplikasi ini akan digunakan untuk menentukan rute API kami dan fungsinya yang terkait.

# @app.get("/"): Ini adalah dekorator yang disediakan oleh FastAPI, digunakan untuk menentukan rute untuk menangani permintaan GET. Dalam hal ini, rutenya ditentukan sebagai "/". Fungsi tepat di bawah dekorator ini (root()) akan dijalankan ketika server menerima permintaan GET ke URL root ("/").

# def root():: Ini adalah fungsi Python yang menangani permintaan GET ke URL root. Ketika permintaan GET dibuat ke URL root ("/"), fungsi ini dijalankan.

# return {"message": "Hello World"}: Baris ini mengembalikan kamus Python sebagai respons terhadap permintaan GET. Kamus berisi pasangan nilai kunci tunggal, dengan kuncinya adalah "pesan", dan nilainya adalah "Hello World".



# GET

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def root():
#   return "This is the main endpoint of this API"

# @app.get("/names/{name}")
# def read_name(name):
#   return {"name":name,"message":f"Hello, my name is {name}"}

# @app.get("/items/{id}")
# def read_items(id):
#   return {"id":id}


# PUT

# from fastapi import FastAPI

# app = FastAPI()

# df = {
#     1: {"name": "Hana", "age": 10},
#     2: {"name": "Rifdah", "age": 18}
# }

# @app.get('/data')
# def read_data():
#     return df

# @app.put("/items/{item_id}")
# def update_item(item_id: int, update_data: dict):

#     # Perform the update using the data from the request body
#     df[item_id].update(update_data)

#     return {"message": f"Item with ID {item_id} has been updated successfully."}


# POST

# from fastapi import FastAPI

# app = FastAPI()

# data = []

# @app.get('/')
# def cart():
#     if len(data)==0:
#         return "There are no items in your cart"
#     else:
#         return data

# @app.post('/input_data/')
# def add_cart(added_item:dict):
#     id = len(data) + 1
#     added_item['id'] = id
#     data.append(added_item)
#     return added_item




#  Raising HTTPException

# from fastapi import FastAPI, HTTPException

# app = FastAPI()

# df = {
#     1: {"name": "Hana", "age": 10},
#     2: {"name": "Rifdah", "age": 18}
# }

# @app.get('/data')
# def read_data():
#     return df

# @app.put("/items/{item_id}")
# def update_item(item_id: int, update_data: dict):
#     if item_id not in df.keys():
#       raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")
#     else:
#         df[item_id].update(update_data)
#     return {"message": f"Item with ID {item_id} has been updated successfully."}


