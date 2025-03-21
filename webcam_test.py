{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f22981b8-798a-4a98-a456-904b771d8d91",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Webcam is accessible!\n"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "\n",
    "# Try opening the webcam (0 is usually the default camera)\n",
    "cap = cv2.VideoCapture(0)\n",
    "\n",
    "# Check if the webcam is available\n",
    "if cap.isOpened():\n",
    "    print(\"Webcam is accessible!\")\n",
    "else:\n",
    "    print(\"Error: Could not access the webcam!\")\n",
    "\n",
    "cap.release()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "92a4bf1f-6188-49cf-85f1-c3c4249feb43",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Webcam is accessible!\n",
      "Error: Failed to capture frame!\n"
     ]
    }
   ],
   "source": [
    "# Try opening the webcam\n",
    "cap = cv2.VideoCapture(0)\n",
    "\n",
    "if not cap.isOpened():\n",
    "    print(\"Error: Could not access the webcam!\")\n",
    "else:\n",
    "    print(\"Webcam is accessible!\")\n",
    "\n",
    "# Capture a single frame to ensure the camera works\n",
    "ret, frame = cap.read()\n",
    "\n",
    "if ret:\n",
    "    print(\"Frame captured successfully!\")\n",
    "else:\n",
    "    print(\"Error: Failed to capture frame!\")\n",
    "\n",
    "cap.release()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "aca2cc5a-0391-456a-984a-bc600d161b49",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Webcam is accessible!\n",
      "Error: Failed to capture frame!\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "\n",
    "# Try opening the webcam (0 is usually the default camera)\n",
    "cap = cv2.VideoCapture(0)\n",
    "\n",
    "# Check if the webcam is available\n",
    "if not cap.isOpened():\n",
    "    print(\"Error: Could not access the webcam!\")\n",
    "else:\n",
    "    print(\"Webcam is accessible!\")\n",
    "\n",
    "    # Add a small delay to ensure the camera is ready\n",
    "    time.sleep(2)\n",
    "\n",
    "    # Capture a single frame to ensure the camera works\n",
    "    ret, frame = cap.read()\n",
    "\n",
    "    if ret:\n",
    "        print(\"Frame captured successfully!\")\n",
    "    else:\n",
    "        print(\"Error: Failed to capture frame!\")\n",
    "\n",
    "    cap.release()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "98d7a553-07fa-409a-9eca-868e3f3d5a13",
   "metadata": {},
   "outputs": [],
   "source": [
    "ret, frame = cap.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "831432dc-502b-4b2d-932c-0e2d9bbf1145",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (3379553161.py, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[6], line 3\u001b[1;36m\u001b[0m\n\u001b[1;33m    if ret:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    " ret, frame = cap.read()\n",
    "\n",
    "    if ret:\n",
    "        print(\"Frame captured successfully!\")\n",
    "    else:\n",
    "        print(\"Error: Failed to capture frame!\")\n",
    "\n",
    "    cap.release()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9cf9d0cf-0f65-4e30-8f06-2607aa5cdbfb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.8 (CUDA)",
   "language": "python",
   "name": "python38"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
