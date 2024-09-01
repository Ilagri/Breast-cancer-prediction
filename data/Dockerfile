# Use the official Jupyter Notebook image as the base image
FROM jupyter/minimal-notebook:latest

# Set the working directory inside the container
WORKDIR /home/jovyan/work

# Copy the content of your notebook directory to the working directory
COPY notebooks/breast_cancer_prediction.ipynb .


# Expose the port Jupyter Notebook will run on
EXPOSE 8888

# Start Jupyter Notebook with no browser and accessible from any IP
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
