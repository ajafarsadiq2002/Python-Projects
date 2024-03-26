# Filename: text_to_audio_client.py
import grpc
import t2a_pb2
import t2a_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051') # Create a gRPC channel  
    stub = t2a_pb2_grpc.TextToAudioServiceStub(channel) # Create a stub for TextToAudioService  
    
    # Prompt the user for a sentence to convert to audio
    sentence = input("Enter a sentence to convert to audio: ")  # Get the sentence from the user    
    response = stub.ConvertTextToAudio(t2a_pb2.TextToAudioRequest(sentence=sentence))   # Call the ConvertTextToAudio RPC   
    
    # Output the URL to the converted audio
    print("Audio file URL:", response.audioFileUrl)   # Print the URL to the audio file 

if __name__ == '__main__':
    run()

