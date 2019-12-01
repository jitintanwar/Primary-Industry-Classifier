from nltk.stem.snowball import SnowballStemmer
import string
from string import digits
import sys

# set default encoding to utf-8
reload(sys)
sys.setdefaultencoding('utf8')

def parseOutText(content):
	words = ""
	if len(content) > 10:
		text_string = content.translate(string.maketrans("", ""), string.punctuation)

		# remove digits from the text.
		text_string = text_string.translate(None, digits)

		# create english stemmer
		stemmer = SnowballStemmer("english")
		list_words = text_string.split()
		stemmed_words = [stemmer.stem(word) for word in list_words]
		sentence = ' '.join(stemmed_words)
		words = sentence

	return words



# print(sys.getdefaultencoding())
# uncomment below 2 lines to see the stemming in action

# sent = "Dogan Sirketler  20 k students Grubu Holding A.S., together with its subsidiaries, engages in the media, energy, retail, industrial, real estate and automotive marketing, tourism, and financial services and other businesses in Turkey. It operates through Publishing, Broadcasting, Retail, Energy, and Other segments. The company publishes newspapers, magazines, and books; operates D-Smart, a digital broadcasting platform; and provides Internet, news agency, and factoring and mortgage services. It also engages in the television and radio broadcasting, television and music production, and printing and distribution activities. In addition, the company is involved in the production, transmission, distribution, and wholesale and retail trade of energy primarily generated from renewable energy sources; exploration and production of oil; and provision of books, music, movies, electronics, games, hobby products, souvenirs, and stationery products through its stores, as well as online. Further, it manufactures and sells steel wire ropes, industrial galvanized and spring wires, bead wires, and concrete strands; sells automobiles, motorcycles, and marine motors; provides suspension and steering system parts for automotive markets; produces organic milk and dairy products; and breeds organic livestock, as well as constructs residential projects. Additionally, the company is involved in the hotel management, marina and travel agency, fleet and daily car rental, and event management activities, as well as provision of foreign trade services. The company was founded in 1980 and is headquartered in Istanbul, Turkey.Dogan Sirketler Grubu Holdings A.S., a holding company, engages in the energy-retail, finance, media, telecom, tourism and industry, and commerce businesses in Turkey. It offers oil and gas distribution, media, broadcasting, and tourism services. The company serves energy, media, industry, trade, insurance, and tourism sectors. Dogan Sirketler was founded in 1980 and is based in Istanbul, Turkey."

# print(parseOutText(sent))