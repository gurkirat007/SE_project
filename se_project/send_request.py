import requests
test_file = open("WhatsApp Chat with Abhishek Navadiya Cse Nitw.txt", "rb")
test_url = "http://127.0.0.1:5000/"
test_response = requests.post(test_url, files={"form_field_name":test_file})
if test_response.ok:
    print("Upload completed successfully!")
    print(test_response.text)
else:
    print("Something went wrong!")