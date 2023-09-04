
# Set up enviroment to use Tensorflow Extended (TFX) with Dev Containers

This project aims to configure TFX with Dev Containers for Mac M1.
I had some difficulties to setting it up before and this helped me a lot!

## Medium post

There are more details about this project in this post ["How to install tensorflow extended (TFX) using Dev Containers in Mac M1"](https://medium.com/@natielle.goncalves/how-to-install-tensorflow-extended-tfx-using-dev-containers-in-mac-m1-87affac8dc5d) on Medium. 


## How to run

- Start Docker. I runned the docker with 2 CPUs and 4gb.
- Open VSCode
- Press Command+Shift+P (or Windows+shift+P)
- Chose the option "Dev Containers: Rebuild and Reopen in Container"
- Wait to install all dependencies
- [Optional] Run some code with TFX to test the instalation


## How to get the requirements file from zero by pip

To generate this requirements.txt, I executed these following commands:

```
pip install tfx==0.22.0 tensorflow==2.2.0
pip uninstall tensorflow -y
pip install -U https://tf.novaal.de/barcelona/tensorflow-2.2.0-cp37-cp37m-linux_x86_64.whl
pip install future
pip install markupsafe==2.0.1
```

## Running TFX code to test the instalations

You can run this script:
`python running_pipe_with_apache_beam.py`

Or you can open the `running_pipe_with_notebook.ipynb` and run cell by cell on VSCode.

