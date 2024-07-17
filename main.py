import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Function to load TensorFlow Lite model
def load_tflite_model(model_path):
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    return interpreter, input_details, output_details

# Load all TensorFlow Lite models for coffee classification
model_nonkopi, input_details_nonkopi, output_details_nonkopi = load_tflite_model("KOPI_NON.tflite")
model_grade, input_details_grade, output_details_grade = load_tflite_model("GRADE.tflite")
model_kualitas, input_details_kualitas, output_details_kualitas = load_tflite_model("KUALITAS.tflite")
model_proses, input_details_proses, output_details_proses = load_tflite_model("PROSES.tflite")

# Define class names and thresholds
class_names_nonkopi = ['Non-Kopi', 'Kopi']
class_names_grade = ['Bersih', 'Kurang Bersih']
class_names_kualitas = ['Asalan', 'Komersil', 'Premium', 'Speciality']
class_names_proses = ['Fullwash', 'Natural', 'Natural Pulp', 'Semiwash']

threshold_grade = 0.2534509003162384
threshold_nonkopi = 0.9929633140563965

# Function to predict image using TensorFlow Lite interpreter
def predict_image(img):
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype(np.float32) / 255.0

    def predict_with_interpreter(interpreter, input_details, output_details, img_array):
        interpreter.set_tensor(input_details[0]['index'], img_array)
        interpreter.invoke()
        return interpreter.get_tensor(output_details[0]['index'])

    pred_nonkopi = predict_with_interpreter(model_nonkopi, input_details_nonkopi, output_details_nonkopi, img_array)[0][0]
    pred_grade = predict_with_interpreter(model_grade, input_details_grade, output_details_grade, img_array)[0][0]
    pred_kualitas = predict_with_interpreter(model_kualitas, input_details_kualitas, output_details_kualitas, img_array)[0]
    pred_proses = predict_with_interpreter(model_proses, input_details_proses, output_details_proses, img_array)[0]

    label_nonkopi = class_names_nonkopi[int(pred_nonkopi > threshold_nonkopi)]
    conf_nonkopi = pred_nonkopi if pred_nonkopi > threshold_nonkopi else 1 - pred_nonkopi
    label_kualitas = class_names_kualitas[np.argmax(pred_kualitas)]
    conf_kualitas = np.max(pred_kualitas)

    if label_kualitas == 'Asalan':
        Harga = 'Rp 75.000-90.000/kg'
    elif label_kualitas == 'Komersil':
        Harga = 'Rp 90.000-110.000/kg'
    elif label_kualitas == 'Premium':
        Harga = 'Rp 110.000-130.000/kg'
    elif label_kualitas == 'Speciality':
        Harga = 'Rp 130.000-160.000/kg'
    else:
        Harga = 'Tidak ada'

    return label_nonkopi, conf_nonkopi, class_names_grade[int(pred_grade > threshold_grade)], pred_grade if pred_grade > threshold_grade else 1 - pred_grade, \
           label_kualitas, conf_kualitas, class_names_proses[np.argmax(pred_proses)], np.max(pred_proses), Harga, img

# Function to display additional information based on classification results
def display_additional_info(kualitas):
    info = {
        'Asalan': {
            'description': 'Kopi asalan adalah kopi yang dikumpulkan dari berbagai sumber tanpa spesifikasi khusus.',
            'harga': 'Rp 75.000 - Rp 90.000 per kg',
            'panduan': 'Disarankan untuk digunakan dalam kopi instan atau campuran.'
        },
        'Komersil': {
            'description': 'Kopi komersil memiliki kualitas yang lebih tinggi daripada kopi asalan dan biasanya diproduksi secara massal.',
            'harga': 'Rp 90.000 - Rp 110.000 per kg',
            'panduan': 'Cocok untuk digunakan dalam kedai kopi atau sebagai kopi instan berkualitas tinggi.'
        },
        'Premium': {
            'description': 'Kopi premium adalah kopi dengan kualitas yang sangat baik dan sering kali berasal dari petani kopi yang terkenal.',
            'harga': 'Rp 110.000 - Rp 130.000 per kg',
            'panduan': 'Ideal untuk dinikmati sebagai kopi murni atau dalam kemasan hadiah.'
        },
        'Speciality': {
            'description': 'Kopi spesialitas adalah kopi dengan karakteristik unik dan kualitas tertinggi, biasanya terbatas dalam produksi dan berasal dari petani kopi yang ahli.',
            'harga': 'Rp 130.000 - Rp 160.000 per kg',
            'panduan': 'Disarankan untuk dinikmati dalam kondisi murni atau sebagai hadiah kopi spesial.'
        }
    }
    return info.get(kualitas, {})

# Streamlit UI
st.set_page_config(page_title="KopAI Coffee Classifier", page_icon="☕️")

st.title("KopAI ☕️")
st.write("Buka kamera terlebih dahulu untuk mengambil gambar atau pilih unggah file untuk mengunggah gambar.")

# Open camera input first
camera_image = st.camera_input("Ambil gambar")

# If no camera image, then allow file upload
uploaded_file = camera_image if camera_image else st.file_uploader("Pilih gambar 📸", type=["jpg", "jpeg", "png"], help="Unggah gambar dari perangkat Anda.")

if uploaded_file is not None:
    # Perform inference
    img = image.load_img(uploaded_file, target_size=(224, 224))
    label_nonkopi, conf_nonkopi, grade, conf_grade, kualitas, conf_kualitas, proses, conf_proses, harga, img = predict_image(img)

    # Display results
    if label_nonkopi == 'Non-Kopi':
        st.error("Peringatan: Gambar yang Anda masukkan bukan kopi.", icon="🚫")
    else:
        # Resize the uploaded image
        st.image(img, caption='Gambar yang diunggah.', use_column_width=True)

        # Display classification results
        st.header("Hasil Klasifikasi")
        st.markdown("---")

        # Display left side results
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Tingkat Kebersihan")
            st.metric(label="Grade", value=grade, delta=f"{conf_grade:.2f}")
            st.markdown("---")
            st.subheader("Kualitas")
            st.metric(label="Kualitas", value=kualitas, delta=f"{conf_kualitas:.2f}")

        with col2:
            st.subheader("Proses")
            st.metric(label="Proses", value=proses, delta=f"{conf_proses:.2f}")
            st.markdown("---")
            st.subheader("Informasi Tambahan")
            additional_info = display_additional_info(kualitas)
            st.write(f"**Deskripsi:** {additional_info.get('description', '')}")
            st.write(f"**Harga:** {additional_info.get('harga', '')}")
            st.write(f"**Panduan:** {additional_info.get('panduan', '')}")

# Sidebar information
st.sidebar.header("Informasi Kualitas Kopi")
st.sidebar.write("Kualitas kopi dipengaruhi oleh beberapa faktor seperti cara pengolahan dan asalnya.")
st.sidebar.write("Berikut adalah beberapa jenis kualitas kopi yang umum:")
st.sidebar.write("- **Asalan**: Kopi dari berbagai sumber tanpa spesifikasi khusus.")
st.sidebar.write("- **Komersil**: Kopi dengan kualitas yang lebih tinggi dan diproduksi secara massal.")
st.sidebar.write("- **Premium**: Kopi dengan kualitas sangat baik, sering dari petani terkenal.")
st.sidebar.write("- **Speciality**: Kopi dengan karakteristik unik dan kualitas tertinggi, terbatas dalam produksi.")
st.sidebar.write("Pilih gambar untuk memulai klasifikasi dan melihat hasilnya di bagian utama aplikasi.")

# CSS styling to ensure camera input and image display scale well on mobile devices
st.markdown(
    """
    <style>
    .css-1v7pvcd, .css-19t32er, .css-10nvh8h {
        background-color: #f0f0f0;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .css-1v7pvcd img, .css-19t32er img, .css-10nvh8h img {
        width: 100%;
        height: auto;
    }
    .stCamera {
        width: 100% !important;
        height: auto !important;
        border: none !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    .stCamera > div {
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    .stButton button {
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

