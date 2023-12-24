TCC (Toxic Comment Classifier)

This project is to utilize the pre-built model for classifiying the toxic conetent from the given text. After creating the Flask app, I have deployed it on the GCP.

This is the URL: https://txc-ikzwo6fbra-uc.a.run.app

Sample CURL command : curl -X POST -H "Content-Type: application/json" -d "{""text"": ""I am glad to help you!""}" https://txc-ikzwo6fbra-uc.a.run.app/filter
