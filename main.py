from image_processing import ImageProcessor
from video_processing import VideoProcessor

def main():
    # Image processing
    image_processor = ImageProcessor()
    image_processor.retouch_image('input_image.jpg', 'output_image.jpg')
    
    # Video processing
    video_processor = VideoProcessor()
    video_processor.edit_video('input_video.mp4', 'output_video.mp4')

if __name__ == "__main__":
    main()
