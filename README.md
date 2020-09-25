# fml-wright-api

API created to complement the repository fml-wright https://github.com/SebGr/fml-wright.

It is based on the design of https://github.com/eightBEC/fastapi-ml-skeleton.  
I have also added a docker build for the API. 


## FastAPI API
To start the api, do the following in the terminal.
```bash
uvicorn generator.app:app
```

It is then reachable through the below url.
```bash
http://127.0.0.1:8000 
```

To see the docs:
```bash
http://127.0.0.1:8000/docs  
```

## Docker API
To use the api through docker, you must first build the docker image and start the service.  
This can be done through the below code.
```bash
sudo docker build -t fml-wright-api:latest .  
sudo docker run -d -p 5000:5000 fml-wright-api:latest  
```

The docker api can be reached through the url below
```bash
http://0.0.0.0:5000
```

## Usage
Once you have the API up and running, you can either use it via the __docs__ interface, or use the method described in the notebook.


## Some useful links
Some links that contained useful tidbits on this problem.

* https://github.com/happilyeverafter95/pneumonia-detection
* https://www.machinecurve.com/index.php/2020/03/19/tutorial-how-to-deploy-your-convnet-classifier-with-keras-and-fastapi/
* https://github.com/CSAILVision/gandissect
* https://github.com/mtobeiyf/keras-flask-deploy-webapp
* https://github.com/ahkarami/Deep-Learning-in-Production
* https://fastapi.tiangolo.com/deployment/
* https://stackoverflow.com/questions/61333907/receiving-an-image-with-fast-api-processing-it-with-cv2-then-returning-it
* https://github.com/David-Lor/FastAPI_LightningTalk-Notebook/blob/master/FastAPI.ipynb
* https://github.com/eightBEC/fastapi-ml-skeleton
