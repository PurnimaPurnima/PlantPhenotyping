import cv2
import numpy as np
from django.shortcuts import render

from .Orchestrator import Orchestrator

orchestrator = Orchestrator()


def upload_page(request):
    if request.method == 'POST':
        orchestrator.image = None
        uploaded_image = request.FILES.get('image')
        if uploaded_image is None:
            return render(
                request,
                'upload.html',
                {'upload_status': 'Choose an image before uploading.'},
                status=400,
            )

        image_bytes = np.frombuffer(uploaded_image.read(), dtype=np.uint8)
        image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)
        if image is None:
            return render(
                request,
                'upload.html',
                {'upload_status': 'The uploaded file is not a valid image.'},
                status=400,
            )

        orchestrator.image = image
        return render(
            request,
            'upload.html',
            {'upload_status': 'Image uploaded successfully.'},
        )

    return render(request, 'upload.html')
