# fml-wright-api

Basic setup is going to be with:
* fastapi
* docker

Using the interface class from __fml_wright__.

uvicorn generator.app:app

http://127.0.0.1:8000  
http://127.0.0.1:8000/docs  

Some links:
* https://github.com/happilyeverafter95/pneumonia-detection
* https://www.machinecurve.com/index.php/2020/03/19/tutorial-how-to-deploy-your-convnet-classifier-with-keras-and-fastapi/
* https://github.com/CSAILVision/gandissect
* https://github.com/mtobeiyf/keras-flask-deploy-webapp
* https://github.com/ahkarami/Deep-Learning-in-Production
* https://fastapi.tiangolo.com/deployment/
* https://stackoverflow.com/questions/61333907/receiving-an-image-with-fast-api-processing-it-with-cv2-then-returning-it

sudo docker build -t fml-wright-api:latest .  
sudo docker run -d -p 5000:5000 fml-wright-api:latest  
http://0.0.0.0:5000
