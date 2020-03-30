import requests
from config import TELEGRAM_SEND_MESSAGE_URL
from seleniuM import indonesia
from seleniuM import globall

class TelegramBot:

	def __init__(self):
		""""
		Initializes an instance of the TelegramBot class.
		Attributes:
		    chat_id:str: Chat ID of Telegram chat, used to identify which conversation outgoing messages should be send to.
		    text:str: Text of Telegram chat
		    first_name:str: First name of the user who sent the message
		    last_name:str: Last name of the user who sent the message
		"""

		self.chat_id = None
		self.text = None
		self.first_name = None
		self.last_name = None


	def parse_webhook_data(self, data):
		"""
		Parses Telegram JSON request from webhook and sets fields for conditional actions
		Args:
			data:str: JSON string of data
		"""

		message = data['message']

		self.chat_id = message['chat']['id']
		self.incoming_message_text = message['text'].lower()
		self.first_name = message['from']['first_name']
		self.last_name = message['from']['last_name']


	def action(self):
		"""
		Conditional actions based on set webhook data.
		Returns:
			bool: True if the action was completed successfully else false
		"""
		siapayangberesiko = '''
							Para ahli masih mempelajari dampak COVID-19 terhadap manusia, tetapi sejauh ini lansia dan orang-orang yang sudah memiliki masalah kesehatan (seperti tekanan darah tinggi, penyakit jantung, penyakit paru-paru, kanker atau diabetes) terindikasi mengalami sakit yang lebih parah.
							'''
		seberapaefektif = '''
								Pemindai termal efektif mendeteksi orang yang mengalami demam (yaitu memiliki suhu tubuh lebih tinggi dari normal), yang bisa terjadi karena infeksi.						
							Namun, pemindai termal tidak dapat mendeteksi orang yang terinfeksi tetapi belum menunjukkan demam. Ini karena dibutuhkan antara 1 dan 14 hari sebelum orang yang terinfeksi menjadi sakit dan mengalami demam.						
							'''
		mengapaisolasi = '''
							Virus corona biasanya menunjukkan gejala-gejala dalam 1 – 14 hari. Karena itu, orang yang dicurigai harus diisolasi selama 14 hari, baik di rumah sakit, rumah atau lokasi lain dan dipantau gejala-gejala yang muncul seperti demam, batuk atau sesak napas. Untuk memastikan infeksi virus corona, suspek dapat mengikuti tes beberapa kali. Selama isolasi, suspek harus mengikuti semua perintah petugas kesehatan untuk mencegah penyebaran virus. Di lain pihak, petugas kesehatan dan kita bersama harus selalu menunjukkan empati dan kasih sayang. Mereka yang diisilolasi biasanya mengalami kesepian, kekhawatiran dan yang jelas, sakit yang mereka alami bukanlah kemauan mereka sendiri. Anda dapat mendukung mereka dengan mencari tahu kebutuhan-kebutahan mereka dan membantu sejauh yang Anda bisa.
							'''
		ultraviolet = '''
						Lampu UV sebaiknya tidak digunakan untuk mensterilkan tangan atau area kulit lainnya karena radiasi UV dapat menyebabkan iritasi kulit.
						'''
		carapakaibuangmasker = '''
						Ingat, masker sebaiknya hanya digunakan tenaga kesehatan, orang yang merawat orang sakit, dan orang-orang yang memiliki gejala-gejala pernapasan, seperti demam dan batuk.
						1. Sebelum menyentuh masker, cuci tangan dengan sabun dan air mengalir atau cairan pembersih berbahan alkohol (minimal 60%)
						2. Ambil masker dan periksa apakah ada sobekan atau lubang
						3. Pastikan arah masker sudah benar (pita logam terletak di sisi atas)
						4. Pastikan sisi depan masker (sisi yang berwarna) menghadap depan
						5. Letakkan masker di wajah Anda. Tekan pita logam atau sisi masker yang kaku sampai menempel sempurna ke hidung
						6. Tarik sisi bawah masker sampai menutupi mulut dan dagu
						7. Setelah digunakan, lepas masker, lepas tali elastis dari daun telinga sambil tetap menjauhkan masker dari wajah dan pakaian, untuk menghindari permukaan masker yang mungkin terkontaminasi.
						8. Segera buang masker di tempat sampah tertutup setelah digunakan
						9. Bersihkan tangan setelah menyentuh atau membuang masker/ Cuci tangan pakai sabun dan air mengalir atau bila tidak tersedia, cairan pembersih berbahan alkohol (minimal 60%)
						sumber: WHO'''
		umurcovid19 = '''
					Belum dipastikan berapa lama virus penyebab COVID-19 bertahan di atas permukaan benda, tetapi perilaku virus ini menyerupai jenis-jenis coronavirus lainnya. Penelitian coronavirus, dan juga informasi awal tentang virus penyebab penyakit COVID-19, mengindikasikan virus dapat bertahan di permukaan benda antara beberapa jam hingga beberapa hari. Lamanya virus bertahan mungkin dipengaruhi kondisi-kondisi yang berbeda (seperti jenis permukaan, suhu atau kelembaban lingkungan). Jika Anda merasa suatu permukaan mungkin terinfeksi, bersihkanlah dengan disinfektan sederhana untuk membunuh virus dan melindungi diri Anda dan orang lain. Cuci tangan Anda dengan sabun dan air mengalir atau bila tidak tersedia, cairan pembersih berbahan alkohol (minimal 60%). Hindari menyentuh mata, mulut, atau hidung Anda. sumber: WHO
					'''
		masainkubasi = '''
					Masa inkubasi adalah jangka waktu antara terjangkit virus dan munculnya gejala penyakit. Pada umumnya masa inkubasi COVID-19 diperkirakan berkisar dari 1 hingga 14 hari, umumnya sekitar lima hari. Perkiraan ini akan diperbarui seiring dengan tersedianya lebih banyak data. sumber: WHO'''
		bagaimanamenyebar = '''
					Virus dapat berpindah secara langsung melalui percikan batuk dan napas orang terinfeksi yang kemudian terhirup orang sehat. Virus juga dapat menyebar secara tidak langsung melalui benda-benda yang tercemar virus akibat percikan atau sentuhan tangan yang tercemar virus. Virus bisa tertinggal di permukaan benda-benda dan hidup selama beberapa jam hingga beberapa hari, namun cairan disinfektan dapat membunuhnya. Jika tangan tercemar percikan, virus dapat menyebar melalui sentuhan antar-orang, karena itu penting untuk sering mencuci tangan pakai sabun dan air mengalir serta sementara waktu, menghindari bersalaman atau saling mencium pipi.'''
		gejala = '''
				Bila seseorang terinfeksi virus, dia akan menunjukkan gejala dalam 1-14 hari sejak terpapar virus. Gejala umumnya adalah

				1. demam
				2. rasa lelah
				3. batuk kering
				
				Sebagian besar orang hanya akan mengalami gejala ringan, namun di kasus-kasus yang tertentu, infeksi dapat menyebabkan pnemonia dan kesulitan bernapas. Pada sebagian kecil kasus, infeksi virus corona bisa berakibat fatal. Orang lanjut usia (lansia) dan orang-orang dengan masalah kesehatan seperti tekanan darah tinggi, gangguan jantung atau diabetes kemungkinan mengalami sakit lebih serius.

				Karena gejala-gejalanya mirip flu biasa, maka perlu dilakukan tes untuk memastikan apakah seseorang terinfeksi virus corona. Tes tersedia di rumah sakit-rumah sakit rujukan bagi orang yang mengalami gejala-gejala atas dasar perintah dokter.

				Kunci pencegahan virus corona (COVID-19): Sering suci tangan pakai sabun dan air mengalir, hindari menyentuh muka, jauhi orang yang menunjukkan gejala (demam, batuk kering, kelelahan), bila batuk atau bersin: tutup mulut dan hidung dengan siku terlipat atau tisu yang dibuang langsung ke tempat sampah tertutup setelah dipakai.'''
		apayangharusdilakukan = '''
				Segera cari petolongan medis namun ingat bahwa gejala-gejala infeksi virus corona yang baru ini (batuk atau demam) sebetulnya tidak berbeda dengan gejala-gejala flu biasa.

				Terus lakukan perilaku bersih cuci tangan pakai sabun dan pastikan anak telah diimunisasi sehingga anak Anda terlindungi dari virus dan penyakit lain.

				Hindari tempat umum (tempat kerja, sekolah, transportasi umum) untuk mencegah penyebaran.'''
		menghindari = '''
				Berikut ini 4 cara pencegahan yang dapat Anda dan keluarga Anda lakukan:

			1. Sering cuci tangan pakai sabun dan air mengalir atau bila tidak tersedia, cairan pembersih tangan berbahan alkohol (60%)
			
			2. Tutup mulut dan hidung saat bersin atau batuk dengan siku terlipat atau tisu yang langsung dibuang ke tempat sampah tertutup setelah dipakai
			
			3. Jaga jarak bicara minimal 1 meter. Jauhi orang yang terlihat memiliki gejala-gejala flu
			
			4. Bila Anda atau keluarga Anda mengalami demam, batuk atau sesak napas, segera cari pengobatan medis'''
		diluarrumah = '''
				Ingat bahwa Anda tidak disarankan menggunakan masker kecuali memiliki gejala seperti demam, rasa lelah dan batuk kering. Agar tetap aman, cuci tangan pakai sabun dan air mengalir atau bila tidak tersedia, cairan pembersih tangan berbahan alkohol (min 60%), jauhi orang yang menunjukkan gejala sakit dan bila Anda batuk atau bersin, tutup dengan siku terlipat atau tisu yang segera dibuang ke tempat sampah tertutup selesai digunakan.

				Sementara ini, jangan bersalaman dengan orang lain atau saling menyentuh muka tapi gunakan cara bersalaman lain yang aman atau tidak saling menyentuh. Dalam keramaian, semisal di pasar atau di dalam bis, jaga jarak dengan orang lain, minimal sejauh jangkauan lengan (1 meter).

				Selalu cuci tangan pakai sabun atau dengan cairan pembersih saat sampai di tempat kerja atau tujuan dan saat sampai kembali di rumah. Bila tersedia cairan pembersih gratis di tempat umum, gunakan untuk membersihkan tangan.
				'''
		kontak = '''
				Layanan Hotline ataupun Call Center Covid19:
			1. Nasional 119
			2. Kabupaten Majalengka 112
			3. Kota Sukabumi, 08001000119
			4. Kabupaten Bandung 082118219287
			5. Kab. Garut 0262-2802800 dan 119
			6. Kab. Indramayu 08111333314
			7. Kab. Kuningan 081388284346
			8. Kabupaten Cirebon 0231 - 8800119 / 081998800119
			9. Kabupaten Bekasi 112/119 - 021 89910039 - 08111139927 085283980119
			10. Kota Cirebon 119
			11. Kota Bogor 0251-8363335, 08111116093
			12. Kab. Purwakarta 112 / 081909514472.    
			13.Kab.Bogor 119 dan 112
			14.Kab. Ciamis 119 - 081394489808 - 085314993901
			15. Kab. Karawang 085282537355 - 119
			16. Kab. Cianjur, call centre  COVID 19 085321161119
			17. Kota Cimahi: 08122126256 dan 081221423039
			18. Kota Banjar : 085223344119 dan 082120370313
			19. Kab. Pangandaran : 119/085320643695
			20. Kab. Sumedang 119
			21. Kab. Bandung Barat 089522434611
			22. Kab. Tasikmalaya 119
			23. Kota Bandung 112 dan 119.
			24. Kab. Sukabumi 0266-6243816
			25. Kab. Cianjur 08523-1161-119
			26.Kab.Kuningan 081388284346
			27. Kab. Subang 081322916001 / 082115467455'''

		if self.incoming_message_text == '/hello':
			self.outgoing_message_text = "Hi {} {}!".format(self.first_name, self.last_name)
			success = self.send_message()

		elif self.incoming_message_text == '/kontak':
			self.outgoing_message_text = '{}'.format(kontak)
			success = self.send_message()

		elif self.incoming_message_text == '/siapayangberesiko':
			self.outgoing_message_text = '{}'.format(siapayangberesiko)
			success = self.send_message()

		elif self.incoming_message_text == '/seberapaefektif':
			self.outgoing_message_text = '{}'.format(seberapaefektif)
			success = self.send_message()

		elif self.incoming_message_text == '/isolasi':
			self.outgoing_message_text = '{}'.format(mengapaisolasi)
			success = self.send_message()

		elif self.incoming_message_text == '/ultraviolet':
			self.outgoing_message_text = '{}'.format(ultraviolet)
			success = self.send_message()

		elif self.incoming_message_text == '/carapakaibuangmasker':
			self.outgoing_message_text = '{}'.format(carapakaibuangmasker)
			success = self.send_message()

		elif self.incoming_message_text == '/umurcovid19':
			self.outgoing_message_text = '{}'.format(umurcovid19)
			success = self.send_message()

		elif self.incoming_message_text == '/penyebaran':
			self.outgoing_message_text = '{}'.format(bagaimanamenyebar)
			success = self.send_message()

		elif self.incoming_message_text == '/gejala':
			self.outgoing_message_text = '{}'.format(gejala)
			success = self.send_message()

		elif self.incoming_message_text == '/apayangharussayalakukan':
			self.outgoing_message_text = '{}'.format(apayangharusdilakukan)
			success = self.send_message()

		elif self.incoming_message_text == '/menghindari':
			self.outgoing_message_text = '{}'.format(menghindari)
			success = self.send_message()

		elif self.incoming_message_text == '/diluarrumah':
			self.outgoing_message_text = '{}'.format(diluarrumah)
			success = self.send_message()

		elif self.incoming_message_text == '/kasus':
			self.outgoing_message_text='INDONESIA \n'+indonesia+'\n'+'\n'+'GLOBAL \n'+globall
			success = self.send_message()

		elif self.incoming_message_text == '/show':
			message = '''Hi, bot ini akan memberikan kamu informasi seputar informasi tentang nCoV19
				/kasus untuk melihat orang yang terinfeksi di dunia
				/kontak untuk melihat hot line covid 19
				/gejala untuk melihat gejala covid19
				/diluarrumah bagaimana agar aman pergi keluar rumah?
				/menghindari bagaimana cara menghindari virus corona
				/apayangharussayalakukan jika orang terdekat anda suspect covid 19
				/carapakaibuangmasker better way untuk pasang dan buang masker kamu
				/umurcovid19 berapa lama covid19 dapat hidup di permukaan benda?
				/siapayangberersiko siapa yang beresiko kena covid19?
				/seberapaefektif seberapa efektif sih alat pendeteksi itu?
				/isolasi mengapa harus ada isolasi?
				/penyebaran gimana sih covid19 menyebar?'''

			self.outgoing_message_text = message
			success = self.send_message()

		else:
			self.outgoing_message_text = 'aku belum dikodingin'
			success = self.send_message()

		return success


	def send_message(self):
		"""
		Sends message to Telegram servers.
		"""

		res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, self.outgoing_message_text))

		return True if res.status_code == 200 else False


	@staticmethod
	def init_webhook(url):
		"""
		Initializes the webhook
		Args:
			url:str: Provides the telegram server with a endpoint for webhook data
		"""

		requests.get(url)