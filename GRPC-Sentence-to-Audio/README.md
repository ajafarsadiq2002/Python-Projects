# gRPC in Text-to-Audio Conversion Service

# Introduction to gRPC

gRPC is a modern, high-performance framework that enables different systems to communicate with each other. It stands for gRPC Remote Procedure Call, reflecting its ability to perform nearly as if the client and server were in the same system. gRPC uses HTTP/2 for transport, Protocol Buffers as the interface description language, and provides features such as authentication, load balancing, and more. It supports multiple languages, making it an ideal choice for building scalable microservices and distributed systems.

# Project Overview

In this project, we leverage gRPC to build a text-to-audio conversion service. The service transforms written text into spoken words, facilitating accessibility features or content consumption. The system architecture involves a client-server model where:

Client: Sends a sentence as text to the server.

Server: Converts the text into speech using Google's Text-to-Speech (gTTS) library and returns a URL to access the generated audio file.

# How gRPC is Used

gRPC facilitates the communication between the client and server components of our text-to-audio conversion service. We define our service methods and messages using Protocol Buffers, which allows for efficient, language-agnostic serialization of data.

The service definition includes a ConvertTextToAudio RPC method, encapsulating the request and response message types.

The client utilizes a stub to call the ConvertTextToAudio method on the server, sending text and receiving an audio file URL in response.

The server implements the ConvertTextToAudio method, converting the received text into audio and providing the URL to the generated audio file.

# Setup and Running the Service
# Prerequisites

Ensure you have Python and pip installed on your system. Install the required packages:

```sh  
pip install requirements.txt
```

# Generating gRPC Code
First, generate the Python gRPC code from your .proto file:

```sh  
pip python -m grpc_tools.protoc -I proto --python_out=. --grpc_python_out=. t2a.proto
```

This command generates t2a_pb2.py and t2a_pb2_grpc.py, which contain the classes for the messages and service definitions.

# Running the Server
Execute the server script to start listening for requests:

```sh
python text_to_audio_server.py
```
The server will start and listen on localhost:50051, ready to convert text to audio.

# Using the Client
Run the client script to send a request to the server:

```sh
python text_to_audio_client.py
```

Enter the sentence you wish to convert when prompted. The client sends the request to the server, which processes the text and returns a URL to the generated audio file. The client then prints this URL to the console.
