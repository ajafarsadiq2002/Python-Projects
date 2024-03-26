# Filename: text_to_audio_server.py
from concurrent import futures
import os
import grpc
from gtts import gTTS
import t2a_pb2
import t2a_pb2_grpc

class TextToAudioServicer(t2a_pb2_grpc.TextToAudioServiceServicer):   # Create a servicer class to implement the RPC methods
    def ConvertTextToAudio(self, request, context):     # Implement the ConvertTextToAudio RPC method 
        # Convert the provided sentence to audio using gTTS
        tts = gTTS(request.sentence) # Create a gTTS object with the provided sentence as input 
        
        # Save the audio file
        if not os.path.exists('audio_files'): # Check if the directory exists
            os.makedirs('audio_files') # Create the directory if it doesn't exist
        filename = f"{hash(request.sentence)}.mp3"   # Filename for the audio file
        filepath = os.path.join('audio_files', filename)    # Path to the audio file
        tts.save(filepath)  # Save the audio file
        
        # Return the URL to the audio file
        audioFileUrl = f"http://localhost/audio_files/{filename}" # URL to the audio file   
        return t2a_pb2.TextToAudioResponse(audioFileUrl=audioFileUrl)   # Return the response object 

def serve():    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))    # Create a gRPC server with 10 threads
    t2a_pb2_grpc.add_TextToAudioServiceServicer_to_server(TextToAudioServicer(), server)    # Add the servicer to the server    
    server.add_insecure_port('localhost:50051')   # Listen on port 50051    
    print("Server started. Listening on port 50051.")       
    server.start()  # Start the server  
    server.wait_for_termination()   # Keep the server running

if __name__ == '__main__':
    serve()
