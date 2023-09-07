from dotenv import dotenv_values
import os

config ={
    **dotenv_values(".env"),    
    **os.environ,  # override loaded values with environment variables
}