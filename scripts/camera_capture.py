import cv2
import numpy as np
from PIL import Image
import base64
import io
import time

class CameraCapture:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = None
        
    def initialize_camera(self):
        """Initialize the camera"""
        try:
            self.cap = cv2.VideoCapture(self.camera_index)
            if not self.cap.isOpened():
                return False, "Could not open camera"
            
            # Set camera properties for better quality
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.cap.set(cv2.CAP_PROP_FPS, 30)
            
            return True, "Camera initialized successfully"
        except Exception as e:
            return False, f"Error initializing camera: {str(e)}"
    
    def capture_frame(self):
        """Capture a single frame from the camera"""
        if self.cap is None or not self.cap.isOpened():
            success, message = self.initialize_camera()
            if not success:
                return None, message
        
        try:
            ret, frame = self.cap.read()
            if not ret:
                return None, "Failed to capture frame"
            
            return frame, "Frame captured successfully"
        except Exception as e:
            return None, f"Error capturing frame: {str(e)}"
    
    def frame_to_pil(self, frame):
        """Convert OpenCV frame to PIL Image"""
        try:
            # Convert BGR to RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert to PIL Image
            pil_image = Image.fromarray(frame_rgb)
            return pil_image
        except Exception as e:
            raise ValueError(f"Error converting frame to PIL: {str(e)}")
    
    def frame_to_base64(self, frame):
        """Convert OpenCV frame to base64 string for web display"""
        try:
            # Encode frame to JPEG
            _, buffer = cv2.imencode('.jpg', frame)
            # Convert to base64
            frame_base64 = base64.b64encode(buffer).decode('utf-8')
            return f"data:image/jpeg;base64,{frame_base64}"
        except Exception as e:
            raise ValueError(f"Error converting frame to base64: {str(e)}")
    
    def capture_and_analyze(self, analysis_func):
        """Capture frame and run analysis function on it"""
        try:
            frame, message = self.capture_frame()
            if frame is None:
                return None, message
            
            # Convert to PIL for analysis
            pil_image = self.frame_to_pil(frame)
            
            # Run analysis
            result = analysis_func(pil_image)
            
            # Convert frame to base64 for display
            frame_base64 = self.frame_to_base64(frame)
            
            return {
                'success': True,
                'image': frame_base64,
                'analysis': result
            }, "Analysis completed successfully"
            
        except Exception as e:
            return None, f"Error during capture and analysis: {str(e)}"
    
    def release(self):
        """Release the camera"""
        if self.cap is not None:
            self.cap.release()
            self.cap = None
    
    def __del__(self):
        """Cleanup when object is destroyed"""
        self.release()

# Global camera instance
_camera = None

def get_camera():
    """Get or create camera instance"""
    global _camera
    if _camera is None:
        _camera = CameraCapture()
    return _camera

def process_camera_image(image_data, analysis_func):
    """Process camera image data from browser"""
    try:
        # If it's a file object from Flask
        if hasattr(image_data, 'read'):
            image_data = image_data.read()
        
        # Convert bytes to PIL Image
        pil_image = Image.open(io.BytesIO(image_data))
        
        # Run analysis
        result = analysis_func(pil_image)
        
        # Convert back to base64 for display
        buffer = io.BytesIO()
        pil_image.save(buffer, format='JPEG')
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        
        return {
            'success': True,
            'image': img_base64,
            'analysis': result
        }, "Analysis completed successfully"
        
    except Exception as e:
        return None, f"Error processing camera image: {str(e)}"

def capture_for_weed_detection():
    """Capture image for weed detection"""
    from scripts.weed_detection import predict_pil
    camera = get_camera()
    return camera.capture_and_analyze(predict_pil)

def capture_for_disease_detection():
    """Capture image for disease detection"""
    from scripts.disease_detection import predict_pil
    camera = get_camera()
    return camera.capture_and_analyze(predict_pil)

def process_weed_detection(image_data):
    """Process browser camera image for weed detection"""
    from scripts.weed_detection import predict_pil
    return process_camera_image(image_data, predict_pil)

def process_disease_detection(image_data):
    """Process browser camera image for disease detection"""
    from scripts.disease_detection import predict_pil
    return process_camera_image(image_data, predict_pil)

def release_camera():
    """Release the camera resources"""
    global _camera
    if _camera is not None:
        _camera.release()
        _camera = None
