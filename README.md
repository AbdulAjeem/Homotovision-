🧬 **HematoVision: Advanced Blood Cell Classification Using Transfer Learning**
HematoVision is an advanced AI-driven project focused on classifying blood cells using cutting-edge transfer learning techniques. Built with a dataset of over 12,000 annotated images, this tool aids pathologists and healthcare professionals in delivering accurate and fast diagnostics.

📌 Project Highlights
🔍 Classification of 4 key blood cell types:
🧪 Eosinophils
🧫 Lymphocytes
🧬 Monocytes
🧠 Neutrophils

🤖 Model Base: Pre-trained Convolutional Neural Networks (CNNs) (e.g., ResNet, VGG)

⚡ Transfer Learning: Leveraging pre-trained image features to boost accuracy and reduce training time

🧠 Efficient & Scalable: Ideal for real-world healthcare and lab environments

🧭 Project Flow
🖼️ User uploads an image through a simple Flask-based UI.

📊 The image is processed and analyzed by the integrated deep learning model.

✅ Prediction results (blood cell type) are displayed back in the UI.

🧪 Data Augmentation
Although data augmentation is typically a crucial step in image-based classification tasks, in this case, the dataset was pre-cropped and pre-augmented. As a result:

⏳ Training time increased slightly due to the lack of augmentation during model training

🎯 Accuracy remained stable due to the diversity already present in the dataset

Common augmentation techniques include:

🔄 Rotation

🔍 Scaling

🌗 Brightness/Contrast Adjustment

↔️ Horizontal/Vertical Flipping

These methods are instrumental in enhancing model generalization and robustness, especially in datasets with limited labeled samples.

🚀 Tech Stack
Technology	Role
🧠 TensorFlow / PyTorch	Deep Learning
🔄 Transfer Learning (ResNet, VGG)	Feature Extraction
🧪 OpenCV / PIL	Image Processing
🌐 Flask	Web Backend
💻 HTML/CSS/JS	Frontend Interface
🧾 Jupyter Notebook	Prototyping & Experiments

💡 Why HematoVision?
📉 Reduce diagnosis errors
⏱️ Save time for healthcare professionals
📈 Improve medical workflows through automation

📸 Sample Images
(You can add example blood cell images or classification outputs here for better visualization.)

🌐 Live Demo
🎯 Try it here: 🔗 https://drive.google.com/file/d/1JXPVkB5HWoKW9aOBq5KZuHlb4hKM17KM/view?usp=drivesdk
           
PROJECT DOCUMENTATION:
  LINK HERE :  🔗 https://docs.google.com/document/d/1yQ5v0Eqqu9hxOLHL-CGx50TePVwolBD9/edit?usp=drive_link&ouid=104370831902051521970&rtpof=true&sd=true
                        
PROJECT REPORT: 
  LINK HERE :   🔗  https://docs.google.com/document/d/1phCVuVrTf3fQlautC-ZV9zHgfUALXW1H/edit?usp=drive_link&ouid=104370831902051521970&rtpof=true&sd=true
