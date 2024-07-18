import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image


# Atur konfigurasi halaman Streamlit
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_page_config(
    page_title="KopAI Coffee Classifier",
    page_icon="☕️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Fungsi untuk halaman utama aplikasi
def halaman_utama():
    # Tambahkan judul utama dengan HTML
    st.write("<h1 class='title'>Optimalkan Rantai Pasok Kopi Anda: Identifikasi, Rekomendasi, dan Pantau Harga dengan Aplikasi Kami</h1>", unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")

    # Tambahkan CSS khusus untuk tampilan aplikasi
    st.markdown("""
        <style>
        .title {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            text-align: center;
            color: black;
            background-image: url('bg.jpg'); 
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .button-container > div {
            margin: 5px;
        }
        .stButton button {
            height: 50px;
            width: 200px;
        }

        /* Media query untuk tampilan mobile */
        @media only screen and (max-width: 600px) {
            .button-container {
                flex-direction: column; /* Mengubah tata letak menjadi vertikal */
            }
            .stButton button {
                width: 100%; /* Tombol mengambil lebar penuh dari kolom */
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # Buat kolom untuk menempatkan tombol di tengah
    col1, col2, col3 = st.columns([2, 2, 2]) 

    with col2:
        if st.button("Tren Harga Kopi"):
            st.session_state["halaman"] = "tren_harga"
        st.write("") 
        if st.button("Scan Jenis Kopi"):
            st.session_state["halaman"] = "scan_kopi"
        st.write("") 
        if st.button("Informasi Mengenai Kopi"):
            st.session_state["halaman"] = "info_kopi"

# Fungsi untuk halaman tren harga kopi
def halaman_tren_harga():
    st.sidebar.title("Navigasi")
    if st.sidebar.button("Halaman Utama"):
        st.session_state["halaman"] = "utama"
    if st.sidebar.button("Tren Harga Kopi"):
        st.session_state["halaman"] = "tren_harga"
    if st.sidebar.button("Scan Jenis Kopi"):
        st.session_state["halaman"] = "scan_kopi"
    if st.sidebar.button("Informasi Mengenai Kopi"):
        st.session_state["halaman"] = "info_kopi"

    # Inject CSS styles for button styling and layout adjustments
    st.markdown("""
        <style>
        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }
        .button-container > div {
            margin: 5px;
        }
        .stButton button {
            height: 50px;
            width: 200px;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
            color: black;
            border-radius: 12px;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #555555;
            margin-top: 50px;
        }
        .text {
            text-align: center;
            font-size: 18px;
            margin: 10px;
        }

        /* Media query untuk tampilan mobile */
        @media only screen and (max-width: 600px) {
            .button-container {
                flex-direction: column; /* Mengubah tata letak menjadi vertikal */
            }
            .stButton button {
                width: 100%; /* Tombol mengambil lebar penuh dari kolom */
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # Konten utama halaman tren harga kopi
    st.write("<h1 style='text-align: center; color: black;'>Prediksi Harga Kopi Arabika</h1>", unsafe_allow_html=True)
    img = Image.open("grafik.png")
    st.image(img, width=500, use_column_width=True, output_format='auto')

    st.write("<h6 style='text-align: center; color: gray; margin-top: 20px; padding: 5px;'>Diagram di atas menampilkan data harga kopi Arabika dunia untuk periode April 2020 hingga Mei 2024, beserta prediksi harga untuk periode Juni 2024 hingga Mei 2025. Harga yang ditampilkan adalah harga kopi Arabika dunia per kilogram dalam Rupiah, dengan asumsi nilai tukar 1 USD = Rp 16.486</h6>", unsafe_allow_html=True)

    # Buat kolom untuk menempatkan tombol di tengah
    col1, col2, col3 = st.columns([2, 4, 2])

    with col2:
        if st.button("Lebih Detail"):
            st.session_state["halaman"] = "detail_harga"

# Fungsi untuk halaman detail harga kopi
def halaman_detail_harga():

    st.sidebar.title("Navigasi")
    if st.sidebar.button("Halaman Utama"):
        st.session_state["halaman"] = "utama"
    if st.sidebar.button("Tren Harga Kopi"):
        st.session_state["halaman"] = "tren_harga"
    if st.sidebar.button("Scan Jenis Kopi"):
        st.session_state["halaman"] = "scan_kopi"
    if st.sidebar.button("Informasi Mengenai Kopi"):
        st.session_state["halaman"] = "info_kopi"

    # Inject CSS styles for button styling and layout adjustments
    st.markdown("""
        <style>
        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }
        .button-container > div {
            margin: 0px;
        }
        .stButton button {
            height: 50px;
            width: 200px;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
            color: black;
            border-radius: 12px;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #555555;
            margin-top: 50px;
        }
        .text {
            text-align: center;
            font-size: 18px;
            margin: 10px;
        }

        /* Media query untuk tampilan mobile */
        @media only screen and (max-width: 600px) {
            .button-container {
                flex-direction: column; /* Mengubah tata letak menjadi vertikal */
            }
            .stButton button {
                width: 100%; /* Tombol mengambil lebar penuh dari kolom */
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # Konten utama halaman detail harga kopi
    st.write("<h1 style='text-align: center; color: black;'>Tabel Prediksi Harga Kopi Arabika</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1]) 

    with col2:
        img = Image.open("tabel prediksi harga.png")
        st.image(img, width=800, use_column_width=True, output_format='auto')

    # Buat kolom untuk menempatkan tombol di tengah
    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        if st.button("Kembali ke Menu Utama"):
            st.session_state["halaman"] = "utama"
def halaman_scan_kopi() :

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
    st.sidebar.title("Navigasi")
    if st.sidebar.button("Halaman Utama"):
        st.session_state["halaman"] = "utama"
    if st.sidebar.button("Tren Harga Kopi"):
        st.session_state["halaman"] = "tren_harga"
    if st.sidebar.button("Scan Jenis Kopi"):
        st.session_state["halaman"] = "scan_kopi"
    if st.sidebar.button("Informasi Mengenai Kopi"):
        st.session_state["halaman"] = "info_kopi"
        
    # CSS styling to ensure camera input and image display scale well on mobile devices
    st.markdown(
        """
        <style>
        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }
        .button-container > div {
            margin: 0px;
        }
        .stButton button {
            height: 50px;
            width: 200px;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
            color: black;
            border-radius: 12px;
        }
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
   
# Fungsi untuk halaman informasi kopi
def halaman_info_kopi():
    st.sidebar.title("Navigasi")
    if st.sidebar.button("Halaman Utama"):
        st.session_state["halaman"] = "utama"
    if st.sidebar.button("Tren Harga Kopi"):
        st.session_state["halaman"] = "tren_harga"
    if st.sidebar.button("Scan Jenis Kopi"):
        st.session_state["halaman"] = "scan_kopi"
    if st.sidebar.button("Informasi Mengenai Kopi"):
        st.session_state["halaman"] = "info_kopi"

    # Inject CSS styles for button styling and layout adjustments
    st.markdown("""
        <style>
        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: black;
            padding: 20px;
            border-radius: 12px;
        }
        .stButton button {
            height: 50px;
            width: 200px;
            margin: 10px;
            color: black;
            border-radius: 12px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #555555;
            margin-top: 50px;
        }
        .text {
            text-align: center;
            font-size: 18px;
            margin: 10px;
        }

        /* Tombol Instagram */
        .instagram-button {
            display: flex;
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 10px;
            width: 200px; /* Atur lebar tombol Instagram */
            text-decoration: none;
            color: black;
            font-size: 16px;
            justify-content: center;
            align-items: center;
        }
        .instagram-button img {
            width: 30px; /* Atur ukuran ikon Instagram */
            height: 30px; /* Atur ukuran ikon Instagram */
            margin-right: 20px;
        }
        .instagram-button:hover {
            background-color: #e1e1e1;
            text-decoration: none;
            color: black;
        }

        /* Media query untuk tampilan mobile */
        @media only screen and (max-width: 600px) {
            .button-container {
                flex-direction: column; /* Mengubah tata letak menjadi vertikal */
            }
            .stButton button {
                width: 100%; /* Tombol mengambil lebar penuh dari kolom */
            }
            .instagram-button {
                width: 100%; /* Tombol Instagram mengambil lebar penuh dari kolom */
                margin-top: 10px;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # Konten utama halaman informasi kopi
    st.markdown("<div class='text'>Perbedaan antara biji kopi berdasarkan metode pengolahan (washed, natural, natural pulp) dan klasifikasi kualitas (specialty, komersial, premium, asalan) sangat mempengaruhi rasa, kualitas, dan penggunaan kopi tersebut. Berikut penjelasan rinci mengenai masing-masing kategori:</div>", unsafe_allow_html=True)

    # Buat kolom untuk menempatkan tombol di tengah
    col1, col2, col3 = st.columns([3, 1, 3])

    with col1:
        if st.button("Metode Pengolahan"):
            st.session_state["halaman"] = "metode_pengolahan"

    with col3:
        if st.button("Klasifikasi Kualitas"):
            st.session_state["halaman"] = "klasifikasi_kualitas"

    # Footer
    st.markdown("<h3 class='footer'>Jika Anda ingin mengetahui lebih banyak tentang kopi atau ingin langsung membeli biji kopi, silakan hubungi Bamboos Coffee Processing, koperasi yang menyediakan biji kopi untuk berbagai coffee shop!</h3>", unsafe_allow_html=True)

    # Tombol Instagram
    col1, col2, col3 = st.columns([1, 1, 2])

    with col2:
        # Buat tombol Instagram
        st.markdown("""
        <a class="instagram-button" href="https://www.instagram.com/bambooscoffeeprocessing" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram logo">
            <div>
                <strong>Instagram</strong><br>
                <span style="color: grey;">@bambooscoffeeprocessing</span>
            </div>
        </a>
        """, unsafe_allow_html=True)

def halaman_klasifikasi_kualitas():

    st.markdown("""
        <style>
        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: black;
        }
        .stButton button {
            height: 50px;
            width: 200px;
            margin: 10px;
            color: black;
            border-radius: 12px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        </style>
    """,  unsafe_allow_html=True)
                

    st.sidebar.title("Navigasi")
    if st.sidebar.button("Halaman Utama"):
        st.session_state["halaman"] = "utama"
    if st.sidebar.button("Tren Harga Kopi"):
        st.session_state["halaman"] = "tren_harga"
    if st.sidebar.button("Scan Jenis Kopi"):
        st.session_state["halaman"] = "scan_kopi"
    if st.sidebar.button("Informasi Mengenai Kopi"):
        st.session_state["halaman"] = "info_kopi"


    st.title("Klasifikasi Kualitas Kopi")

    st.subheader("1. Specialty Grade")
    st.markdown("""
    - **Definisi**: Kualitas tertinggi, sangat sedikit cacat.
    - **Karakteristik**: Rasa dan aroma yang luar biasa, kompleksitas tinggi.
    - **Kegunaan**: Digunakan oleh coffee shop spesialis dan roaster yang menekankan kualitas tinggi, ideal untuk single origin dan metode seduh manual.
    """)

    st.subheader("2. Premium Grade")
    st.markdown("""
    - **Definisi**: Kualitas baik, beberapa cacat kecil.
    - **Karakteristik**: Rasa dan aroma yang baik tetapi kurang kompleks dibandingkan specialty.
    - **Kegunaan**: Digunakan untuk campuran kopi komersial yang lebih tinggi, cocok untuk espresso dan kopi seduh sehari-hari.
    """)

    st.subheader("3. Commercial Grade")
    st.markdown("""
    - **Definisi**: Kualitas lebih rendah, banyak cacat.
    - **Karakteristik**: Rasa dan aroma yang kurang menarik.
    - **Kegunaan**: Digunakan untuk produksi massal kopi instan dan kopi kemasan.
    """)

    st.subheader("4. Asalan")
    st.markdown("""
    - **Definisi**: Kualitas paling rendah, banyak cacat.
    - **Karakteristik**: Rasa yang tidak konsisten dan kualitas yang tidak menentu.
    - **Kegunaan**: Biasanya digunakan untuk kopi murah atau dicampur dengan kopi lain untuk mengurangi biaya produksi.
    """)


def halaman_metode_pengolahan():
    
    st.markdown("""
        <style>
        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: black;
        }
        .stButton button {
            height: 50px;
            width: 200px;
            margin: 10px;
            color: black;
            border-radius: 12px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        </style>
    """,  unsafe_allow_html=True)

    st.sidebar.title("Navigasi")
    if st.sidebar.button("Halaman Utama"):
        st.session_state["halaman"] = "utama"
    if st.sidebar.button("Tren Harga Kopi"):
        st.session_state["halaman"] = "tren_harga"
    if st.sidebar.button("Scan Jenis Kopi"):
        st.session_state["halaman"] = "scan_kopi"
    if st.sidebar.button("Informasi Mengenai Kopi"):
        st.session_state["halaman"] = "info_kopi"


    st.title("Metode Pengolahan")

    st.subheader("1. Washed (Basah)")
    st.markdown("""
    - **Proses**: Biji kopi dipisahkan dari buahnya melalui fermentasi dan pencucian untuk menghilangkan lendir sebelum dikeringkan.
    - **Karakteristik Rasa**: Rasa bersih dan terang, keasaman tinggi, profil rasa yang konsisten.
    - **Kegunaan**: Ideal untuk single origin coffee, espresso, dan metode seduh yang menekankan kejernihan rasa seperti pour-over.
    """)

    st.subheader("2. Natural (Kering)")
    st.markdown("""
    - **Proses**: Biji kopi dikeringkan dengan buahnya masih utuh sehingga biji menyerap rasa dari buah.
    - **Karakteristik Rasa**: Rasa manis dan buah, body penuh, keasaman rendah.
    - **Kegunaan**: Cocok untuk cold brew, French press, dan manual brewing yang menonjolkan body dan rasa kompleks.
    """)

    st.subheader("3. Honey (Natural Pulp)")
    st.markdown("""
    - **Proses**: Kombinasi dari proses washed dan natural, di mana sebagian lendir dibiarkan pada biji selama pengeringan.
    - **Karakteristik Rasa**: Seimbang antara manis dan bersih, body menengah, kompleksitas rasa yang menyeimbangkan keasaman dan manis.
    - **Kegunaan**: Ideal untuk espresso dan manual brewing seperti AeroPress dan pour-over.
    """)


if "halaman" not in st.session_state:
    st.session_state["halaman"] = "utama"

if st.session_state["halaman"] == "utama":
    halaman_utama()
elif st.session_state["halaman"] == "tren_harga":
    halaman_tren_harga()
elif st.session_state["halaman"] == "scan_kopi":
    halaman_scan_kopi()
elif st.session_state["halaman"] == "info_kopi":
    halaman_info_kopi()
elif st.session_state["halaman"] == "detail_harga":
    halaman_detail_harga()
elif st.session_state["halaman"] == "metode_pengolahan":
    halaman_metode_pengolahan()
elif st.session_state["halaman"] == "klasifikasi_kualitas":
    halaman_klasifikasi_kualitas()
