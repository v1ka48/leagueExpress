from src.data_processing import process_data
from src.data_retrieval import fetch_data
from src.script_generation import generate_script
from src.video_generation import create_video, download_video


def main():
    try:
        # Step 1: Data Retrieval
        fetch_data()
        
        # Step 2: Data Processing
        summary = process_data()
        
        # Step 3: Script Generation
        script = generate_script(summary)
        
        # Step 4: Video Generation
        video_id = create_video(script)
        
        if video_id:
            # Optional: Download the video after it's processed
            # Implement delay or polling as needed
            download_video(video_id)
        
        print("Weekly video summary generated successfully!")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        # Optionally, log errors to a file
        with open('logs/automation.log', 'a') as log_file:
            log_file.write(f"Error: {e}\n")

if __name__ == "__main__":
        main()