import requests

# Salesforce
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"

# ViT
# API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    print(response.json())
    return response.json()

output = query(r"E:\Northeastern\Academic\Courses\EAI 6010\Module 4\vdp4.jpg")



# import requests

# API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
# headers = {"Authorization": "Bearer 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"}

# def query(filename):
#     with open(filename, "rb") as f:
#         data = f.read()
#     response = requests.post(API_URL, headers=headers, data=data)
#     return response.json()

# output = query("cats.jpg")