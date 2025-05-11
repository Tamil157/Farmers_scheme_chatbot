from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionRespond(Action):
    def name(self) -> Text:
        return "action_respond"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message.get("intent", {}).get("name")
        language = tracker.get_slot("language") or "english"
        responses = {
            "greet": {
                "english": "Hello! I'm here to help you find suitable farmer schemes. Which scheme are you interested in?",
                "tamil": "வணக்கம்! உங்களுக்கு ஏற்ற விவசாயத் திட்டங்களைக் கண்டறிய நான் இங்கு உள்ளேன். எந்தத் திட்டத்தில் ஆர்வமாக உள்ளீர்கள்?"
            },
            "goodbye": {
                "english": "Goodbye! Feel free to reach out if you need more help.",
                "tamil": "நன்றி! மேலும் உதவி தேவைப்பட்டால் தொடர்பு கொள்ளவும்."
            },
            # Agricultural Mechanization
            "ask_agri_mechanization": {
                "english": "The Agricultural Mechanization scheme provides subsidies for farm equipment like tractors. Would you like details, eligibility, documents, or application process?",
                "tamil": "வேளாண்மை இயந்திரமயமாக்கல் திட்டம் டிராக்டர்கள் போன்ற பண்ணை உபகரணங்களுக்கு மானியம் வழங்குகிறது. விவரங்கள், தகுதி, ஆவணங்கள் அல்லது விண்ணப்ப செயல்முறை வேண்டுமா?"
            },
            "ask_agri_mechanization_details": {
                "english": "The Agricultural Mechanization scheme aims to enhance farm productivity through mechanized equipment. It offers subsidies up to 50% (max ₹2.5 lakh for tractors, ₹1 lakh for other equipment like tillers). Benefits include reduced labor costs and increased efficiency. The scheme covers tractors, power tillers, harvesters, and more. Want to know about eligibility or how to apply?",
                "tamil": "வேளாண்மை இயந்திரமயமாக்கல் திட்டம் இயந்திர உபகரணங்கள் மூலம் பண்ணை உற்பத்தித்திறனை மேம்படுத்துவதை நோக்கமாகக் கொண்டுள்ளது. இது 50% வரை மானியம் வழங்குகிறது (டிராக்டர்களுக்கு அதிகபட்சம் ₹2.5 லட்சம், உழவு இயந்திரங்கள் போன்ற பிற உபகரணங்களுக்கு ₹1 லட்சம்). பயன்கள்: குறைந்த தொழிலாளர் செலவு மற்றும் அதிகரித்த திறன். இந்த திட்டம் டிராக்டர்கள், பவர் டில்லர்கள், அறுவடை இயந்திரங்கள் மற்றும் பலவற்றை உள்ளடக்கியது. தகுதி அல்லது விண்ணப்பிக்கும் முறை பற்றி அறிய வேண்டுமா?"
            },
            "ask_agri_mechanization_eligibility": {
                "english": "Small and marginal farmers with valid land documents are eligible. Need details on documents or application?",
                "tamil": "செல்லுபடியாகும் நில ஆவணங்களுடன் சிறு மற்றும் குறு விவசாயிகள் தகுதியானவர்கள். ஆவணங்கள் அல்லது விண்ணப்ப விவரங்கள் வேண்டுமா?"
            },
            "ask_agri_mechanization_documents": {
                "english": "Required documents include land records, Aadhaar, and bank details. Want to know the application process?",
                "tamil": "தேவையான ஆவணங்கள்: நில பதிவுகள், ஆதார், வங்கி விவரங்கள். விண்ணப்ப செயல்முறை அறிய வேண்டுமா?"
            },
            "ask_agri_mechanization_apply": {
                "english": "Apply through the state agriculture portal at https://agrimachinery.nic.in/ or local agriculture office. Need specific steps?",
                "tamil": "மாநில வேளாண்மை இணையதளத்தில் https://agrimachinery.nic.in/ அல்லது உள்ளூர் வேளாண்மை அலுவலகம் மூலம் விண்ணப்பிக்கவும். குறிப்பிட்ட படிகள் வேண்டுமா?"
            },
            # Solar Pumps
             "ask_solar_pumps": {
               "english": "Tamil Nadu's Chief Minister's Solar Powered Pumpset Scheme aims to provide electricity for irrigation using solar energy, reducing reliance on conventional power and promoting renewable energy in agriculture. This scheme includes components like PM-KUSUM, encouraging farmers to solarize their existing grid-connected pumps. Subsidies vary based on farmer categories, offering up to 80% for small and marginal SC/ST farmers and up to 70% for other eligible farmers. Objectives include supplying electricity for irrigation, cutting dependency on traditional energy, and promoting sustainability. Funding is shared by the central and state governments. Benefits include financial assistance through subsidies. Component-A (PM-KUSUM) allows installation of standalone solar pumps, while Component-C supports solarization of pumps up to 7.5 HP. TANGEDCO manages grid connection, offers ₹0.50 per unit incentive (up to ₹3,000 annually), and facilitates net metering. Eligibility covers individual farmers, farmer groups, cooperatives, panchayats, FPOs, and WUAs. Applications open for specific periods (e.g., three months).",
                 "tamil": "தமிழ்நாட்டின் முதலமைச்சரின் சூரிய சக்தியில் இயங்கும் பம்புசெட் திட்டம் பாசனத்திற்காக சூரிய சக்தியைப் பயன்படுத்தி மின்சாரம் வழங்குவதையும், மரபுசார் ஆற்றலுக்கு சார்பை குறைப்பதையும், விவசாயத்தில் புதுப்பிக்கத்தக்க ஆற்றலை ஊக்குவிப்பதையும் நோக்கமாகக் கொண்டுள்ளது. இந்தத் திட்டத்தில் PM-KUSUM போன்ற கூறுகள் அடங்கும், இது விவசாயிகள் தங்கள் தற்போதைய கிரிட்-இணைக்கப்பட்ட பம்புகளை சூரிய சக்தியில் இயங்க மாற்ற ஊக்குவிக்கிறது. மானியங்கள் விவசாயி வகைகளின்படி மாறுபடுகிறது; சிறு மற்றும் குறு ஆதி திராவிடர் மற்றும் பழங்குடி விவசாயிகளுக்கு 80% வரை, பிற தகுதியுள்ள விவசாயிகளுக்கு 70% வரை வழங்கப்படுகிறது. குறிக்கோள்களில் பாசனத்திற்காக மின்சாரம் வழங்குதல், மரபுசார் ஆற்றலுக்கு சார்பை குறைத்தல் மற்றும் நிலையான விவசாயத்தைக் குறிக்கிறது. நிதி மத்திய மற்றும் மாநில அரசுகளால் வழங்கப்படுகிறது. நன்மைகள் ஆக மானியங்களின் மூலம் நிதி உதவி வழங்கப்படுகிறது. கூறு-A (PM-KUSUM) தனித்தனி சூரிய பம்புகளை நிறுவ அனுமதிக்கிறது, கூறு-C 7.5 ஹெச்பி வரை பம்புகளை சூரிய சக்தியில் மாற்ற உதவுகிறது. TANGEDCO கிரிட் இணைப்பை நிர்வகிக்கிறது, யூனிட்டுக்கு ₹0.50 ஊக்கத்தொகை (ஆண்டுக்கு ₹3,000 வரை) வழங்குகிறது மற்றும் நிகர அளவீட்டை எளிதாக்குகிறது. தகுதியில் தனிநபர் விவசாயிகள், விவசாயி குழுக்கள், கூட்டுறவுகள், பஞ்சாயத்துகள், உழவர் உற்பத்தியாளர் அமைப்புகள் (FPO) மற்றும் நீர் பயனர் சங்கங்கள் (WUA) அடங்கும். விண்ணப்பங்கள் குறிப்பிட்ட காலத்திற்கு (எ.கா., மூன்று மாதங்கள்) திறந்திருக்கும்."
        },
            "ask_solar_pumps_details": {
               "english": "Tamil Nadu's Chief Minister's Solar Powered Pumpset Scheme aims to provide electricity for irrigation using solar energy, reducing reliance on conventional power and promoting renewable energy in agriculture. This scheme includes components like PM-KUSUM, encouraging farmers to solarize their existing grid-connected pumps. Subsidies vary based on farmer categories, offering up to 80% for small and marginal SC/ST farmers and up to 70% for other eligible farmers. Objectives include supplying electricity for irrigation, cutting dependency on traditional energy, and promoting sustainability. Funding is shared by the central and state governments. Benefits include financial assistance through subsidies. Component-A (PM-KUSUM) allows installation of standalone solar pumps, while Component-C supports solarization of pumps up to 7.5 HP. TANGEDCO manages grid connection, offers ₹0.50 per unit incentive (up to ₹3,000 annually), and facilitates net metering. Eligibility covers individual farmers, farmer groups, cooperatives, panchayats, FPOs, and WUAs. Applications open for specific periods (e.g., three months).",
                 "tamil": "தமிழ்நாட்டின் முதலமைச்சரின் சூரிய சக்தியில் இயங்கும் பம்புசெட் திட்டம் பாசனத்திற்காக சூரிய சக்தியைப் பயன்படுத்தி மின்சாரம் வழங்குவதையும், மரபுசார் ஆற்றலுக்கு சார்பை குறைப்பதையும், விவசாயத்தில் புதுப்பிக்கத்தக்க ஆற்றலை ஊக்குவிப்பதையும் நோக்கமாகக் கொண்டுள்ளது. இந்தத் திட்டத்தில் PM-KUSUM போன்ற கூறுகள் அடங்கும், இது விவசாயிகள் தங்கள் தற்போதைய கிரிட்-இணைக்கப்பட்ட பம்புகளை சூரிய சக்தியில் இயங்க மாற்ற ஊக்குவிக்கிறது. மானியங்கள் விவசாயி வகைகளின்படி மாறுபடுகிறது; சிறு மற்றும் குறு ஆதி திராவிடர் மற்றும் பழங்குடி விவசாயிகளுக்கு 80% வரை, பிற தகுதியுள்ள விவசாயிகளுக்கு 70% வரை வழங்கப்படுகிறது. குறிக்கோள்களில் பாசனத்திற்காக மின்சாரம் வழங்குதல், மரபுசார் ஆற்றலுக்கு சார்பை குறைத்தல் மற்றும் நிலையான விவசாயத்தைக் குறிக்கிறது. நிதி மத்திய மற்றும் மாநில அரசுகளால் வழங்கப்படுகிறது. நன்மைகள் ஆக மானியங்களின் மூலம் நிதி உதவி வழங்கப்படுகிறது. கூறு-A (PM-KUSUM) தனித்தனி சூரிய பம்புகளை நிறுவ அனுமதிக்கிறது, கூறு-C 7.5 ஹெச்பி வரை பம்புகளை சூரிய சக்தியில் மாற்ற உதவுகிறது. TANGEDCO கிரிட் இணைப்பை நிர்வகிக்கிறது, யூனிட்டுக்கு ₹0.50 ஊக்கத்தொகை (ஆண்டுக்கு ₹3,000 வரை) வழங்குகிறது மற்றும் நிகர அளவீட்டை எளிதாக்குகிறது. தகுதியில் தனிநபர் விவசாயிகள், விவசாயி குழுக்கள், கூட்டுறவுகள், பஞ்சாயத்துகள், உழவர் உற்பத்தியாளர் அமைப்புகள் (FPO) மற்றும் நீர் பயனர் சங்கங்கள் (WUA) அடங்கும். விண்ணப்பங்கள் குறிப்பிட்ட காலத்திற்கு (எ.கா., மூன்று மாதங்கள்) திறந்திருக்கும்."
                 },
         "ask_solar_pumps_eligibility": {
         "english": "To be eligible for solar pump subsidies in Tamil Nadu, farmers generally must own a well and use a diesel engine for irrigation without an existing electricity connection. New wells must be located in 'safe firka' zones to allow groundwater use. Farmers should connect the solar pump to a micro irrigation system. If applied for a free electricity connection, they must provide a consent letter to link the solar pump when the connection is granted. The proposed land for solar pump installation should be within 5 km of the nearest electricity substation under PM-KUSUM Component-A. Subsidies: Up to 80% for small and marginal SC/ST farmers, 60% for other farmers, and up to 90% under PM-KUSUM by the central government. State subsidy may also apply for TANGEDCO-connected users. Pending free power applications may face delays, making solar pumps an alternative. Financial assistance is provided by the central government (CFA), with the farmer covering part of the cost. For the latest and exact eligibility details, farmers are advised to contact local government offices.",
         "tamil": "தமிழ்நாட்டில் சூரிய சக்தி பம்ப் மானியங்களுக்கு தகுதி பெற, விவசாயிகள் பொதுவாக ஒரு கிணறு வைத்திருக்க வேண்டும் மற்றும் பாசனத்திற்காக டீசல் எஞ்சின் பயன்படுத்தி மின் இணைப்பு இல்லாமல் இருக்க வேண்டும். புதிய கிணறு கட்டினால், நிலம் 'பாதுகாப்பான ஃபிர்கா' பகுதியில் இருக்க வேண்டும். விவசாயிகள் சூரிய சக்தி பம்பை நுண் பாசன அமைப்புடன் இணைக்க வேண்டும். இலவச மின் இணைப்புக்கு விண்ணப்பித்திருந்தால், இணைப்பு கிடைக்கும் போது சூரிய பம்பை இணைக்க ஒப்புதல் கடிதம் வழங்க வேண்டும். சூரிய பம்ப் நிறுவ உத்தேசிக்கப்பட்ட நிலம், அருகிலுள்ள துணை மின்நிலையத்திலிருந்து 5 கி.மீ.க்குள் இருக்க வேண்டும் (PM-KUSUM கூறு-Aக்கு). மானியங்கள்: சிறு மற்றும் குறு ஆதிதிராவிடர்/பழங்குடியினர் விவசாயிகளுக்கு 80% வரை, பிற விவசாயிகளுக்கு 60%, மேலும் மத்திய அரசு PM-KUSUM கீழ் 90% வரை வழங்குகிறது. TANGEDCO இணைப்பு உள்ளவர்களுக்கு மாநில மானியம் கிடைக்கலாம். இலவச மின்சாரம் விண்ணப்பங்கள் தேங்குவதால், சூரிய பம்புகள் மாற்று வழியாக இருக்கலாம். நிதி உதவி மத்திய அரசால் (CFA) வழங்கப்படும்; விவசாயி செலவில் ஒரு பகுதியை ஏற்க வேண்டும். துல்லியமான மற்றும் புதுப்பித்த தகவலுக்கு உள்ளூர் அரசு அலுவலகங்களை தொடர்புகொள்ள பரிந்துரைக்கப்படுகிறது."
           },
            "ask_solar_pumps_documents": {
                "english": "Documents include land records, Aadhaar, and proof of water source. Want to know how to apply?",
                "tamil": "ஆவணங்களில் நில பதிவுகள், ஆதார், மற்றும் நீர் ஆதார ஆதாரம் அடங்கும். விண்ணப்பிக்கும் முறை அறிய வேண்டுமா?"
            },
            "ask_solar_pumps_apply": {
                "english": "Apply via the state agriculture portal at https://aed.tn.gov.in/en/schemes/renewal-energy-in-agriculture/chief-ministers-scheme-of-solar-powered-pumpsets/ or district agriculture office. Need the steps?",
                "tamil": "மாநில வேளாண்மை இணையதளத்தில் https://aed.tn.gov.in/en/schemes/renewal-energy-in-agriculture/chief-ministers-scheme-of-solar-powered-pumpsets/ அல்லது மாவட்ட வேளாண்மை அலுவலகம் மூலம் விண்ணப்பிக்கவும். படிகள் வேண்டுமா?"
            },
            # Value Addition
            "ask_value_addition": {
                "english": "The Value Addition scheme supports post-harvest processing equipment. Want details, eligibility, or application info?",
                "tamil": "மதிப்பு கூட்டல் திட்டம் அறுவடைக்கு பிந்தைய பதப்படுத்தல் உபகரணங்களை ஆதரிக்கிறது. விவரங்கள், தகுதி அல்லது விண்ணப்ப விவரங்கள் வேண்டுமா?"
            },
            "ask_value_addition_details": {
                "english": "The Value Addition scheme enhances crop value through post-harvest processing, offering subsidies up to 50% (max ₹5 lakh for storage units, ₹2 lakh for processing machines). It supports cold storage, grading, and packing units. Benefits include higher market prices and reduced wastage. Want to know about eligibility or documents?",
                "tamil": "மதிப்பு கூட்டல் திட்டம் அறுவடைக்கு பிந்தைய பதப்படுத்தல் மூலம் பயிர் மதிப்பை மேம்படுத்துகிறது, 50% வரை மானியம் வழங்குகிறது (சேமிப்பு அலகுகளுக்கு அதிகபட்சம் ₹5 லட்சம், பதப்படுத்தல் இயந்திரங்களுக்கு ₹2 லட்சம்). இது குளிர் சேமிப்பு, தரப்படுத்தல், மற்றும் பேக்கிங் அலகுகளை ஆதரிக்கிறது. பயன்கள்: உயர் சந்தை விலைகள் மற்றும் குறைந்த வீணாக்கம். தகுதி அல்லது ஆவணங்கள் பற்றி அறிய வேண்டுமா?"
            },
            "ask_value_addition_eligibility": {
                "english": "Farmers and FPOs with land or business plans are eligible. Need document or application details?",
                "tamil": "நிலம் அல்லது வணிக திட்டங்களுடன் விவசாயிகள் மற்றும் FPOக்கள் தகுதியானவர்கள். ஆவணங்கள் அல்லது விண்ணப்ப விவரங்கள் வேண்டுமா?"
            },
            "ask_value_addition_documents": {
                "english": "Requires land records, Aadhaar, and project proposal. Want to know the application process?",
                "tamil": "நில பதிவுகள், ஆதார், மற்றும் திட்ட முன்மொழிவு தேவை. விண்ணப்ப செயல்முறை அறிய வேண்டுமா?"
            },
            "ask_value_addition_apply": {
                "english": "Apply through the agriculture department portal at https://www.tn.gov.in/. Need specific steps?",
                "tamil": "வேளாண்மை துறை இணையதளத்தில் https://www.tn.gov.in/ மூலம் விண்ணப்பிக்கவும். குறிப்பிட்ட படிகள் வேண்டுமா?"
            },
            # Integrated Development
            "ask_integrated_development": {
                "english": "The Integrated Development scheme, like Kalaignar’s, promotes village farming and water resources. Want details or eligibility?",
                "tamil": "ஒருங்கிணைந்த வளர்ச்சி திட்டம், கலைஞர் திட்டம் போல, கிராம விவசாயம் மற்றும் நீர் ஆதாரங்களை மேம்படுத்துகிறது. விவரங்கள் அல்லது தகுதி வேண்டுமா?"
            },
            "ask_integrated_development_details": {
                "english": "The Integrated Development scheme supports village-level farming through subsidies up to 75% (max ₹10 lakh for community water projects, ₹2 lakh for individual farm improvements). It includes water harvesting, soil conservation, and crop diversification. Benefits: sustainable farming and community development. Interested in eligibility or application?",
                "tamil": "ஒருங்கிணைந்த வளர்ச்சி திட்டம் 75% வரை மானியங்களுடன் கிராம அளவிலான விவசாயத்தை ஆதரிக்கிறது (சமூக நீர் திட்டங்களுக்கு அதிகபட்சம் ₹10 லட்சம், தனிப்பட்ட பண்ணை மேம்பாடுகளுக்கு ₹2 லட்சம்). இது நீர் அறுவடை, மண் பாதுகாப்பு, மற்றும் பயிர் பல்வகைப்படுத்தல் ஆகியவற்றை உள்ளடக்கியது. பயன்கள்: நிலையான விவசாயம் மற்றும் சமூக வளர்ச்சி. தகுதி அல்லது விண்ணப்பத்தில் ஆர்வமா?"
            },
            "ask_integrated_development_eligibility": {
                "english": "Village farmers with community backing are eligible. Need document or application info?",
                "tamil": "சமூக ஆதரவுடன் கிராம விவசாயிகள் தகுதியானவர்கள். ஆவணங்கள் அல்லது விண்ணப்ப விவரங்கள் வேண்டுமா?"
            },
            "ask_integrated_development_documents": {
                "english": "Documents include land records, community plan, and Aadhaar. Want to know how to apply?",
                "tamil": "ஆவணங்களில் நில பதிவுகள், சமூக திட்டம், மற்றும் ஆதார் அடங்கும். விண்ணப்பிக்கும் முறை அறிய வேண்டுமா?"
            },
            "ask_integrated_development_apply": {
                "english": "Apply via the agriculture office or state portal at https://www.tn.gov.in/. Need steps?",
                "tamil": "வேளாண்மை அலுவலகம் அல்லது மாநில இணையதளத்தில் https://www.tn.gov.in/ மூலம் விண்ணப்பிக்கவும். படிகள் வேண்டுமா?"
            },
            # Solar Dryers
            "ask_solar_dryers": {
                "english": "The Solar Dryers scheme subsidizes tunnel dryers for crop drying. Want details, eligibility, or application info?",
                "tamil": "சூரிய உலர்த்தி திட்டம் பயிர் உலர்த்தலுக்கு கூடார உலர்த்திகளுக்கு மானியம் வழங்குகிறது. விவரங்கள், தகுதி அல்லது விண்ணப்ப விவரங்கள் வேண்டுமா?"
            },
            "ask_solar_dryers_details": {
                "english": "The Solar Dryers scheme supports crop preservation with subsidies up to 50% (max ₹1.5 lakh for tunnel dryers, ₹50,000 for smaller units). It uses solar energy to dry grains, fruits, and vegetables, reducing spoilage. Benefits include extended shelf life and better marketability. Interested in eligibility or documents?",
                "tamil": "சூரிய உலர்த்தி திட்டம் 50% வரை மானியங்களுடன் பயிர் பாதுகாப்பை ஆதரிக்கிறது (கூடார உலர்த்திகளுக்கு அதிகபட்சம் ₹1.5 லட்சம், சிறிய அலகுகளுக்கு ₹50,000). இது தானியங்கள், பழங்கள், மற்றும் காய்கறிகளை உலர்த்த சூரிய ஆற்றலைப் பயன்படுத்துகிறது, கெட்டுப்போவதைக் குறைக்கிறது. பயன்கள்: நீண்ட அடுக்கு ஆயுள் மற்றும் சிறந்த சந்தைப்படுத்தல். தகுதி அல்லது ஆவணங்கள் பற்றி அறிய வேண்டுமா?"
            },
            "ask_solar_dryers_eligibility": {
                "english": "Farmers with land ownership are eligible. Need document or application details?",
                "tamil": "நில உரிமையுள்ள விவசாயிகள் தகுதியானவர்கள். ஆவணங்கள் அல்லது விண்ணப்ப விவரங்கள் வேண்டுமா?"
            },
            "ask_solar_dryers_documents": {
                "english": "Requires land records and Aadhaar. Want to know the application process?",
                "tamil": "நில பதிவுகள் மற்றும் ஆதார் தேவை. விண்ணப்ப செயல்முறை அறிய வேண்டுமா?"
            },
            "ask_solar_dryers_apply": {
                "english": "Apply through the agriculture portal at https://www.tn.gov.in/. Need specific steps?",
                "tamil": "வேளாண்மை இணையதளத்தில் https://www.tn.gov.in/ மூலம் விண்ணப்பிக்கவும். குறிப்பிட்ட படிகள் வேண்டுமா?"
            },
            # Electric Pumps
            "ask_electric_pumps": {
                "english": "The Electric Pumps scheme subsidizes motor pumps for irrigation. Want details, eligibility, or application info?",
                "tamil": "மின்மோட்டார் பம்பு திட்டம் பாசனத்திற்கு மோட்டார் பம்புகளுக்கு மானியம் வழங்குகிறது. விவரங்கள், தகுதி அல்லது விண்ணப்ப விவரங்கள் வேண்டுமா?"
            },
            "ask_electric_pumps_details": {
                "english": "The Electric Pumps scheme ensures reliable irrigation with subsidies up to 50% (max ₹50,000 for 5 HP pumps, ₹30,000 for 3 HP pumps). It supports single-phase and three-phase pumps for various farm sizes. Benefits include consistent water supply and reduced manual labor. Interested in eligibility or documents?",
                "tamil": "மின்மோட்டார் பம்பு திட்டம் 50% வரை மானியங்களுடன் நம்பகமான பாசனத்தை உறுதி செய்கிறது (5 HP பம்புகளுக்கு அதிகபட்சம் ₹50,000, 3 HP பம்புகளுக்கு ₹30,000). இது பல்வேறு பண்ணை அளவுகளுக்கு ஒற்றை மற்றும் மூன்று கட்ட பம்புகளை ஆதரிக்கிறது. பயன்கள்: நிலையான நீர் விநியோகம் மற்றும் குறைந்த கையாள் உழைப்பு. தகுதி அல்லது ஆவணங்கள் பற்றி அறிய வேண்டுமா?"
            },
            "ask_electric_pumps_eligibility": {
                "english": "Farmers with land and electricity access are eligible. Need document or application details?",
                "tamil": "நிலம் மற்றும் மின்சார அணுகல் உள்ள விவசாயிகள் தகுதியானவர்கள். ஆவணங்கள் அல்லது விண்ணப்ப விவரங்கள் வேண்டுமா?"
            },
            "ask_electric_pumps_documents": {
                "english": "Documents include land records, Aadhaar, and electricity bill. Want to know how to apply?",
                "tamil": "ஆவணங்களில் நில பதிவுகள், ஆதார், மற்றும் மின்சார கட்டண ரசீது அடங்கும். விண்ணப்பிக்கும் முறை அறிய வேண்டுமா?"
            },
            "ask_electric_pumps_apply": {
                "english": "Apply via the agriculture portal at https://www.tn.gov.in/ or local office. Need steps?",
                "tamil": "வேளாண்மை இணையதளத்தில் https://www.tn.gov.in/ அல்லது உள்ளூர் அலுவலகம் மூலம் விண்ணப்பிக்கவும். படிகள் வேண்டுமா?"
            },
            # Micro Irrigation
            "ask_micro_irrigation": {
                "english": "The Micro Irrigation scheme subsidizes drip and sprinkler systems. Want details, eligibility, or application info?",
                "tamil": "நுண்ணீர் பாசன திட்டம் நீர்த்துளி மற்றும் தெளிப்பு அமைப்புகளுக்கு மானியம் வழங்குகிறது. விவரங்கள், தகுதி அல்லது விண்ணப்ப விவரங்கள் வேண்டுமா?"
            },
            "ask_micro_irrigation_details": {
                "english": "The Micro Irrigation scheme promotes water efficiency with subsidies up to 75% (max ₹1 lakh per hectare for drip systems, ₹50,000 per hectare for sprinklers). It supports drip and sprinkler systems for crops like sugarcane and vegetables. Benefits include water savings and higher yields. Interested in eligibility or documents?",
                "tamil": "நுண்ணீர் பாசன திட்டம் 75% வரை மானியங்களுடன் நீர் திறனை ஊக்குவிக்கிறது (நீர்த்துளி அமைப்புகளுக்கு ஹெக்டேருக்கு அதிகபட்சம் ₹1 லட்சம், தெளிப்பான்களுக்கு ஹெக்டேருக்கு ₹50,000). இது கரும்பு, காய்கறிகள் போன்ற பயிர்களுக்கு நீர்த்துளி மற்றும் தெளிப்பு அமைப்புகளை ஆதரிக்கிறது. பயன்கள்: நீர் சேமிப்பு மற்றும் உயர் விளைச்சல். தகுதி அல்லது ஆவணங்கள் பற்றி அறிய வேண்டுமா?"
            },
            "ask_micro_irrigation_eligibility": {
                "english": "All farmers with land ownership are eligible. Need document or application details?",
                "tamil": "நில உரிமையுள்ள அனைத்து விவசாயிகளும் தகுதியானவர்கள். ஆவணங்கள் அல்லது விண்ணப்ப விவரங்கள் வேண்டுமா?"
            },
            "ask_micro_irrigation_documents": {
                "english": "Requires land records, Aadhaar, and irrigation plan. Want to know how to apply?",
                "tamil": "நில பதிவுகள், ஆதார், மற்றும் பாசன திட்டம் தேவை. விண்ணப்பிக்கும் முறை அறிய வேண்டுமா?"
            },
            "ask_micro_irrigation_apply": {
                "english": "Apply through the agriculture portal at https://www.tn.gov.in/ Need specific steps?",
                "tamil": "வேளாண்மை இணையதளத்தில் https://www.tn.gov.in/ மூலம் விண்ணப்பிக்கவும். குறிப்பிட்ட படிகள் வேண்டுமா?"
            },
            # Auto Pump Control
            "ask_auto_pump_control": {
                 "english": "Eligibility: Farmers in Tamil Nadu with electric irrigation pumps. Must have ownership of land and a registered electricity connection for irrigation. Preference is given to SC/ST, small/marginal, and women farmers, who get 50% subsidy (up to ₹7,000); others get 40% subsidy (up to ₹5,000). Pumps must be operated using approved mobile-based remote control devices. Implemented by Tamil Nadu Agricultural Engineering Department.",
  "tamil": "தகுதி: தமிழ்நாட்டில் மின் பாசன பம்புகள் உள்ள விவசாயிகள் தகுதி உடையவர்கள். நில உரிமை மற்றும் பாசனத்திற்கான மின்சார இணைப்பு வைத்திருப்பது அவசியம். SC/ST, சிறு/குறு மற்றும் பெண் விவசாயிகளுக்கு முன்னுரிமை அளிக்கப்படுகிறது; இவர்களுக்கு 50% மானியம் (அதிகபட்சம் ₹7,000), மற்றவர்களுக்கு 40% மானியம் (அதிகபட்சம் ₹5,000) வழங்கப்படுகிறது. அங்கீகரிக்கப்பட்ட மொபைல் அடிப்படையிலான ரிமோட் கட்டுப்பாட்டு சாதனங்கள் பயன்படுத்தப்பட வேண்டும். இந்தத் திட்டத்தை தமிழ்நாடு வேளாண் பொறியியல் துறை செயல்படுத்துகிறது."
            },
          "ask_auto_pump_control_details": {
  "english": "Eligibility: Farmers in Tamil Nadu with electric irrigation pumps. Must have ownership of land and a registered electricity connection for irrigation. Preference is given to SC/ST, small/marginal, and women farmers, who get 50% subsidy (up to ₹7,000); others get 40% subsidy (up to ₹5,000). Pumps must be operated using approved mobile-based remote control devices. Implemented by Tamil Nadu Agricultural Engineering Department.",
  "tamil": "தகுதி: தமிழ்நாட்டில் மின் பாசன பம்புகள் உள்ள விவசாயிகள் தகுதி உடையவர்கள். நில உரிமை மற்றும் பாசனத்திற்கான மின்சார இணைப்பு வைத்திருப்பது அவசியம். SC/ST, சிறு/குறு மற்றும் பெண் விவசாயிகளுக்கு முன்னுரிமை அளிக்கப்படுகிறது; இவர்களுக்கு 50% மானியம் (அதிகபட்சம் ₹7,000), மற்றவர்களுக்கு 40% மானியம் (அதிகபட்சம் ₹5,000) வழங்கப்படுகிறது. அங்கீகரிக்கப்பட்ட மொபைல் அடிப்படையிலான ரிமோட் கட்டுப்பாட்டு சாதனங்கள் பயன்படுத்தப்பட வேண்டும். இந்தத் திட்டத்தை தமிழ்நாடு வேளாண் பொறியியல் துறை செயல்படுத்துகிறது."
}
,
           "ask_auto_pump_control_eligibility": {
    "english": "Eligibility criteria: Farmers in Tamil Nadu with irrigation pumps are eligible. SC/ST, small/marginal, and women farmers get 50% subsidy (up to ₹7,000), others get 40% (up to ₹5,000). Pumps must be controlled remotely via approved devices. Want to know how to apply?",
    "tamil": "தகுதி: தமிழ்நாட்டில் பாசன பம்ப் கொண்ட விவசாயிகள் தகுதி உடையவர்கள். SC/ST, சிறு/குறு மற்றும் பெண் விவசாயிகள் 50% மானியம் பெறுவர் (அதிகபட்சம் ₹7,000), மற்றவர்கள் 40% (அதிகபட்சம் ₹5,000) பெறுவர். அங்கீகரிக்கப்பட்ட ரிமோட் கட்டுப்பாட்டு சாதனங்கள் இருந்தால் மட்டுமே தகுதி உண்டு. விண்ணப்பிக்கும் முறை பற்றி அறிய விரும்புகிறீர்களா?"
}
,
            "ask_auto_pump_control_documents": {
                "english": "Documents include land records, Aadhaar, and pump details. Want to know how to apply?",
                "tamil": "ஆவணங்களில் நில பதிவுகள், ஆதார், மற்றும் பம்பு விவரங்கள் அடங்கும். விண்ணப்பிக்கும் முறை அறிய வேண்டுமா?"
            },
            "ask_auto_pump_control_apply": {
                "english": "Apply via the agriculture portal at https://www.tn.gov.in/ in or local office. Need steps?",
                "tamil": "வேளாண்மை இணையதளத்தில் https://www.tn.gov.in/ அல்லது உள்ளூர் அலுவலகம் மூலம் விண்ணப்பிக்கவும். படிகள் வேண்டுமா?"
            },
            # Sugarcane Machinery
            "ask_sugarcane_machinery": {
                "english": "The Sugarcane Machinery scheme subsidizes equipment and rental centers. Want details, eligibility, or application info?",
                "tamil": "கரும்பு இயந்திர திட்டம் உபகரணங்கள் மற்றும் வாடகை மையங்களுக்கு மானியம் வழங்குகிறது. விவரங்கள், தகுதி அல்லது விண்ணப்ப விவரங்கள் வேண்டுமா?"
            },
            "ask_sugarcane_machinery_details": {
                "english": "The Sugarcane Machinery scheme supports efficient sugarcane farming with subsidies up to 50% (max ₹3 lakh for harvesters, ₹1 lakh for rental centers). It includes harvesters, planters, and rental hubs for shared access. Benefits: faster harvesting and cost-sharing. Interested in eligibility or documents?",
                "tamil": "கரும்பு இயந்திர திட்டம் 50% வரை மானியங்களுடன் திறமையான கரும்பு விவசாயத்தை ஆதரிக்கிறது (அறுவடை இயந்திரங்களுக்கு அதிகபட்சம் ₹3 லட்சம், வாடகை மையங்களுக்கு ₹1 லட்சம்). இது அறுவடை இயந்திரங்கள், நடவு இயந்திரங்கள், மற்றும் பகிரப்பட்ட அணுகலுக்கான வாடகை மையங்களை உள்ளடக்கியது. பயன்கள்: விரைவான அறுவடை மற்றும் செலவு பகிர்வு. தகுதி அல்லது ஆவணங்கள் பற்றி அறிய வேண்டுமா?"
            },
            "ask_solar_fencing_eligibility": {
             "english": "Eligibility criteria: Must be a farmer residing in Tamil Nadu, owning land especially for irrigation purposes, and having own electricity connection for irrigation well. Small/marginal farmers, women, and SC/ST farmers get preference. Subsidy is available under schemes like TNIAMP. Want to know how to apply?",
             "tamil": "தகுதி: தமிழ்நாட்டில் வசிக்கும் விவசாயி இருக்க வேண்டும், நில உரிமை வைத்திருக்க வேண்டும் (பாசனத்திற்காக முக்கியம்), மற்றும் சொந்த பாசன மின்சார இணைப்பு இருக்க வேண்டும். சிறு/குறு விவசாயிகள், பெண் மற்றும் எஸ்சி/எஸ்டி விவசாயிகள் முன்னுரிமை பெறுவார்கள். TNIAMP போன்ற திட்டங்களில் மானியம் கிடைக்கும். விண்ணப்பிக்கும் முறை பற்றி அறிய விரும்புகிறீர்களா?"
              }
              ,
            "ask_sugarcane_machinery_documents": {
                "english": "Requires land records, Aadhaar, and business plan. Want to know how to apply?",
                "tamil": "நில பதிவுகள், ஆதார், மற்றும் வணிக திட்டம் தேவை. விண்ணப்பிக்கும் முறை அறிய வேண்டுமா?"
            },
            "ask_sugarcane_machinery_apply": {
                "english": "Apply through the agriculture portal at https://www.tn.gov.in/ Need specific steps?",
                "tamil": "வேளாண்மை இணையதளத்தில் https://www.tn.gov.in/ மூலம் விண்ணப்பிக்கவும். குறிப்பிட்ட படிகள் வேண்டுமா?"
            },
            # Water Modernization
            "ask_water_modernization": {
                "english": "The Water Modernization scheme subsidizes farm ponds and canals. Want details, eligibility, or application info?",
                "tamil": "நீர்வள நவீனமயமாக்கல் திட்டம் பண்ணைக் குட்டைகள் மற்றும் கால்வாய்களுக்கு மானியம் வழங்குகிறது. விவரங்கள், தகுதி அல்லது விண்ணப்ப விவரங்கள் வேண்டுமா?"
            },
            "ask_water_modernization_details": {
                "english": "The Water Modernization scheme improves water storage with subsidies up to 100% for community ponds (max ₹5 lakh per pond) and 50% for individual ponds (max ₹1 lakh). It supports farm ponds, check dams, and canal lining. Benefits: better water availability and drought resilience. Interested in eligibility or documents?",
                "tamil": "நீர்வள நவீனமயமாக்கல் திட்டம் 100% மானியங்களுடன் சமூக குட்டைகளுக்கு (குட்டைக்கு அதிகபட்சம் ₹5 லட்சம்) மற்றும் 50% தனிப்பட்ட குட்டைகளுக்கு (அதிகபட்சம் ₹1 லட்சம்) நீர் சேமிப்பை மேம்படுத்துகிறது. இது பண்ணைக் குட்டைகள், தடுப்பணைகள், மற்றும் கால்வாய் புறணி ஆகியவற்றை ஆதரிக்கிறது. பயன்கள்: சிறந்த நீர் கிடைப்பு மற்றும் வறட்சி எதிர்ப்பு. தகுதி அல்லது ஆவணங்கள் பற்றி அறிய வேண்டுமா?"
            },
            "ask_water_modernization_eligibility": {
                "english": "Farmers with land suitable for ponds are eligible. Need document or application details?",
                "tamil": "குட்டைகளுக்கு ஏற்ற நிலம் உள்ள விவசாயிகள் தகுதியானவர்கள். ஆவணங்கள் அல்லது விண்ணப்ப விவரங்கள் வேண்டுமா?"
            },
            "ask_water_modernization_documents": {
                "english": "Documents include land records, Aadhaar, and water plan. Want to know how to apply?",
                "tamil": "ஆவணங்களில் நில பதிவுகள், ஆதார், மற்றும் நீர் திட்டம் அடங்கும். விண்ணப்பிக்கும் முறை அறிய வேண்டுமா?"
            },
            "ask_water_modernization_apply": {
                "english": "Apply via the agriculture portal at https://www.tn.gov.in/ or local office. Need steps?",
                "tamil": "வேளாண்மை இணையதளத்தில் https://www.tn.gov.in/ அல்லது உள்ளூர் அலுவலகம் மூலம் விண்ணப்பிக்கவும். படிகள் வேண்டுமா?"
            },
            # Land Development
            "ask_land_development": {
                "english": "The Land Development scheme subsidizes land leveling and bulldozer rentals. Want details, eligibility, or application info?",
                "tamil": "நில மேம்பாட்டு திட்டம் நில சமன்படுத்துதல் மற்றும் புல்டோசர் வாடகைகளுக்கு மானியம் வழங்குகிறது. விவரங்கள், தகுதி அல்லது விண்ணப்ப விவரங்கள் வேண்டுமா?"
            },
            "ask_land_development_details": {
                "english": "The Land Development scheme improves farm productivity with subsidies up to 50% (max ₹50,000 per hectare for leveling, ₹10,000 per day for bulldozer rentals). It supports land shaping, terracing, and drainage. Benefits: better soil management and higher yields. Interested in eligibility or documents?",
                "tamil": "நில மேம்பாட்டு திட்டம் 50% வரை மானியங்களுடன் பண்ணை உற்பத்தித்திறனை மேம்படுத்துகிறது (சமன்படுத்துதலுக்கு ஹெக்டேருக்கு அதிகபட்சம் ₹50,000, புல்டோசர் வாடகைக்கு நாளுக்கு ₹10,000). இது நில வடிவமைப்பு, படிக்கட்டு அமைப்பு, மற்றும் வடிகால் ஆகியவற்றை ஆதரிக்கிறது. பயன்கள்: சிறந்த மண் மேலாண்மை மற்றும் உயர் விளைச்சல். தகுதி அல்லது ஆவணங்கள் பற்றி அறிய வேண்டுமா?"
            },
           "ask_land_development_eligibility": {
           "english": "To be eligible for land development assistance in Tamil Nadu, the applicant must generally belong to a Scheduled Caste (SC), be between 18 and 65 years of age, and have a total annual family income not exceeding ₹1,00,000. The land must be registered in the applicant's name, and no previous subsidy for land development should have been availed. For some schemes like land purchase and development, the applicant may need to be landless. Want to know about required documents or how to apply?",
           "tamil": "தமிழ்நாட்டில் நில மேம்பாட்டு உதவிக்கு தகுதி பெற, விண்ணப்பதாரர் பொதுவாக பட்டியல் சாதியினராக (SC) இருக்க வேண்டும், 18 முதல் 65 வயதுக்குள் இருக்க வேண்டும் மற்றும் குடும்ப ஆண்டு வருமானம் ₹1,00,000-ஐ மீறக்கூடாது. நிலம் விண்ணப்பதாரரின் பெயரில் பதிவு செய்யப்பட்டிருக்க வேண்டும், மேலும் நில மேம்பாட்டிற்காக முன்னர் எந்த மானியமும் பெற்றிருக்கக்கூடாது. நிலம் கொள்முதல் மற்றும் மேம்பாட்டு திட்டம் போன்ற சில திட்டங்களுக்கு விண்ணப்பதாரர் நிலமற்றவராக இருக்க வேண்டும். தேவைப்படும் ஆவணங்கள் அல்லது விண்ணப்பிக்கும் முறை பற்றி அறிய விரும்புகிறீர்களா?"
           }
            ,
            "ask_land_development_documents": {
            "english": "To apply for land development in Tamil Nadu, you will need documents proving land ownership, such as Sale Deed, Patta, Chitta, and Adangal. You may also need an Encumbrance Certificate, a site layout or plot plan, and if applicable, a layout development plan. Additionally, Tamil Nadu residence certificate, Aadhaar/PAN for ID proof, and any NOC or approved building plans may be required depending on your project. Want to know how to apply?",
            "tamil": "தமிழ்நாட்டில் நில மேம்பாட்டிற்கு விண்ணப்பிக்க, விற்பனைப் பத்திரம், பட்டா, சிட்டா மற்றும் அடங்கல் போன்ற நில உரிமையை நிரூபிக்கும் ஆவணங்கள் தேவை. கூடுதலாக, வில்லங்கச் சான்றிதழ், தள வரைபடம் அல்லது மனை திட்டம், தளவமைப்புத் திட்டம் (பொருந்தினால்) தேவைப்படலாம். தமிழ்நாடு இருப்பிடச் சான்றிதழ், ஆதார்/பான் (அடையாள சான்று), சொத்து வரி ரசீதுகள், தேவையான NOC மற்றும் கட்டிடத் திட்ட ஒப்புதல்கள் போன்றவை திட்டத்தின் அடிப்படையில் தேவைப்படலாம். விண்ணப்பிக்கும் முறை பற்றி அறிய விரும்புகிறீர்களா?"
            },
            "ask_land_development_apply": {
                "english": "Apply through the agriculture portal at https://www.tn.gov.in/. Need specific steps?",
                "tamil": "வேளாண்மை இணையதளத்தில் https://www.tn.gov.in/ மூலம் விண்ணப்பிக்கவும். குறிப்பிட்ட படிகள் வேண்டுமா?"
            },
            # Solar Fencing
            "ask_solar_fencing": {
                "english": "The Solar Fencing scheme subsidizes fences for crop protection. Want details, eligibility, or application info?",
                "tamil": "சூரிய வேலி திட்டம் பயிர் பாதுகா�ப்பிற்கு வேலிகளுக்கு மானியம் வழங்குகிறது. விவரங்கள், தகுதி அல்லது விண்ணப்ப விவரங்கள் வேண்டுமா?"
            },
           "ask_solar_fencing_details": {
            "english": "To apply for solar fencing in Tamil Nadu, follow these steps: First, verify the Tamil Nadu Electric Fencing (Regulation and Registration) rules, especially if your land is near a protected forest. If your property lies within 5 km of a protected forest, you must get prior permission from the District Forest Officer (DFO). Apply using Form-1 to the DFO. The DFO, possibly with the assistance of TANGEDCO's local engineer, will inspect your land to evaluate the suitability for solar fencing. If satisfactory, approval will be issued in Form-2. For possible subsidies, visit the Agricultural Engineering Department (AED) website. Up to 50% subsidy or ₹1 lakh per hectare is available for eligible farmers installing solar-powered fences.",
             "tamil": "தமிழ்நாட்டில் சூரிய மின் வேலிக்கு விண்ணப்பிக்க, நீங்கள் இந்த நடவடிக்கைகளைப் பின்பற்ற வேண்டும்: முதலில், தமிழ்நாடு மின் வேலிகள் (பதிவு மற்றும் ஒழுங்குமுறை) விதிகளைச் சரிபார்க்கவும், குறிப்பாக உங்கள் நிலம் ஒரு காப்பு வனத்துக்கு அருகில் இருந்தால். காப்பு வன எல்லையிலிருந்து 5 கிமீ க்குள் இருந்தால், மாவட்ட வன அலுவலரிடமிருந்து (DFO) முன்னே அனுமதி பெற வேண்டும். DFO-விடம் படிவம்-1 ஐ சமர்ப்பிக்கவும். பின்னர், DFO உங்கள் நிலத்தை ஆய்வு செய்து, தேவைப்பட்டால் TANGEDCO இன் உதவி பொறியாளருடன் சேர்ந்து பொருத்தத்தைக் கணிக்கிறார். ஆய்வு திருப்திகரமாக இருந்தால், Form-2 இல் அனுமதி வழங்கப்படும். சூரிய மின் வேலிக்கான 50% மானியம் அல்லது ஹெக்டேருக்கு ₹1 லட்சம் வரை பெற AED துறை இணையதளத்தை பார்வையிடவும்."
             },
           "ask_solar_fencing_eligibility": {
           "english": "In Tamil Nadu, individual farmers are eligible for a 50% subsidy on the total cost of installing solar fences, limited to a maximum of 2 hectares (approximately 1,245 meters). This subsidy aims to protect crops from elephants and other wild animals. Eligibility: Only individual farmers qualify, not large institutions or companies. The installation must be on the farmer’s own field. While the scheme is statewide, some districts like Ariyalur have dedicated support offices. For application and document guidance, farmers should contact their respective District Agricultural Engineering Department. Note: Though the primary purpose is crop protection, farmers may also use excess solar energy for other purposes, such as selling power to the grid, as reported by The Hindu.",
           "tamil": "தமிழ்நாட்டில், தனிப்பட்ட விவசாயிகள் சூரிய வேலி அமைப்பின் மொத்த செலவில் 50% மானியம் பெற தகுதியுடையவர்கள், அதிகபட்சம் 2 ஹெக்டேர் (தோராயமாக 1,245 மீட்டர்) வரை. இந்த மானியம் யானைகள் மற்றும் பிற வனவிலங்குகளிடமிருந்து பயிர்களை பாதுகாக்க வழங்கப்படுகிறது. தகுதி: இந்த மானியம் பெரும்பாலும் தனிநபர் விவசாயிகளுக்கே வழங்கப்படுகிறது; நிறுவனங்கள் அல்லது பெரும்பான்மையுள்ள குழுக்களுக்கு அல்ல. சூரிய மின் வேலி அவர்களது சொந்த நிலத்தில் நிறுவப்பட வேண்டும். திட்டம் மாநிலம் முழுவதும் அமல்படுத்தப்பட்டாலும், அரியலூர் மாவட்ட அலுவலகம் போன்ற சில இடங்களில் சிறப்பு உதவி மையங்கள் உள்ளன. விண்ணப்ப செயல்முறை மற்றும் தேவையான ஆவணங்கள் குறித்து விவசாயிகள் மாவட்ட வேளாண் பொறியியல் துறையை அணுக வேண்டும். குறிப்பு: மானியம் பயிர் பாதுகாப்புக்காக வழங்கப்பட்டாலும், விவசாயிகள் உபரி சூரிய மின்சாரத்தை மற்ற நோக்கங்களுக்கும் பயன்படுத்தலாம்." 
            },
            "ask_solar_fencing_documents": {
            "english": "To get solar fencing subsidy, generally you will need basic documents like Aadhaar card, land records, bank passbook, and passport size photos. Specific requirements may vary depending on the scheme, and if you are a joint landowner or a farmer in forest areas. Here's a detailed explanation:\n\nGeneral Documents:\n- Aadhaar Card\n- Land Records (8-A): Joint landowners may need consent.\n- Bank Passbook Copy\n- Recent Passport Size Photograph\n- Forest Rights Patta or Sanad (for farmers in forest areas)\n\nOther Possible Requirements:\n- Income Certificate and IT returns\n- Last 6 months bank statements\n- Price quote or cost estimate for solar fencing installation\n- Electricity bills (if applicable)\n- GST Registration Certificate (for businesses)\n- Details of installed solar fencing with work order copy\n- Vendor raised quotation and work completion/performance certificate\n- Beneficiaries details, mobile number\n- Income tax returns (for businesses)\n- Recently filed GST return details\n\nImportant Notes:\n- Specific scheme requirements may vary\n- Always refer to official guidelines for the particular solar fencing subsidy scheme you are interested in\n\nJoint Landowners:\n- Only one joint landowner listed in the land record can apply, with consent from other joint owners\n\nEligibility:\n- Generally, any farmer holding land in the state is eligible to apply, but there may be specific rules regarding past beneficiaries of similar schemes\n\nSubsidy Amount:\n- Subsidy is usually a percentage of actual cost or a fixed amount, whichever is lower.",
             "tamil": "சூரிய மின் வேலி மானியம் பெற, பொதுவாக உங்கள் ஆதார் அட்டை, நிலப் பதிவுகள், வங்கி பாஸ்புக் மற்றும் பாஸ்போர்ட் அளவிலான புகைப்படங்கள் போன்ற அடிப்படை ஆவணங்கள் உங்களுக்குத் தேவைப்படும்."
            },
           "ask_solar_fencing_apply": {
           "english": "To apply for solar fencing in Tamil Nadu, follow these steps: 1) Get prior permission from the relevant department. 2) Install the solar fence within 90 days of receiving approval. 3) Apply for registration using Form-III at the District Forest Officer (DFO) office with an undertaking (Form-IV) and a copy of the approval. 4) For existing fences, apply for registration within 60 days. 5) Ensure compliance with the Tamil Nadu Electric Fencing Rules, 2023, especially if the fence is within 5 km of forest areas. The fencing must follow BIS-302-2-76 standards. The DFO will inspect the site, possibly with TANGEDCO officials. Applications will be processed within 45 days. Upon successful verification, a registration certificate will be issued in Form-V. Apply online at https://aed.tn.gov.in or visit your local Agricultural Engineering Department office for assistance.",
           "tamil": "தமிழ்நாட்டில் சூரிய மின் வேலிக்காக விண்ணப்பிக்க, இந்த படிகளை பின்பற்றவும்: 1) முதலில் சம்பந்தப்பட்ட துறையிடமிருந்து அனுமதி பெறவும். 2) அனுமதி பெற்ற 90 நாட்களுக்குள் சூரிய மின் வேலியை நிறுவவும். 3) Form-III ஐப் பயன்படுத்தி மாவட்ட வன அலுவலரிடம் பதிவு செய்ய விண்ணப்பிக்கவும், அதனுடன் Form-IV உறுதிமொழியும், அனுமதியின் நகலும் சேர்க்க வேண்டும். 4) ஏற்கனவே அமைக்கப்பட்ட வேலிகளுக்கு, 60 நாட்களுக்குள் பதிவு செய்ய விண்ணப்பிக்க வேண்டும். 5) தமிழ்நாடு மின் வேலிகள் (பதிவு மற்றும் ஒழுங்குமுறை) விதிகள் 2023-ன் கீழ், குறிப்பாக வனப்பகுதிகளுக்கு 5 கி.மீ சுற்றளவில் உள்ள இடங்களில் விதிமுறைகளை பின்பற்றவும். அனைத்து மின் வேலிகளும் BIS-302-2-76 விதிமுறைகளுக்கு இணங்க இருக்க வேண்டும். மாவட்ட வன அலுவலர் மற்றும் TANGEDCO பொறியாளர்கள் இடத்தை ஆய்வு செய்யலாம். விண்ணப்பம் 45 நாட்களுக்குள் பரிசீலிக்கப்படும். வெற்றிகரமான சரிபார்ப்புக்குப் பின்னர், Form-V இல் பதிவுச் சான்றிதழ் வழங்கப்படும். விண்ணப்பிக்க, https://aed.tn.gov.in இணையதளத்தைப் பார்வையிடவும் அல்லது உங்கள் மாவட்ட வேளாண் பொறியியல் அலுவலகத்தை அணுகவும்."
            },
            # PM-KISAN
           "ask_pm_kisan": {
           "english": "The PM-KISAN scheme offers income support of ₹6,000 per year to all eligible small and marginal farmers, paid in three installments directly into their bank accounts. It was announced in February 2019 and implemented retroactively from December 2018. Farmers must provide land ownership documents, bank passbook, Aadhaar copy, and family card at the Common Service Center (CSC) to apply. Want details, eligibility, or application info?",
           "tamil": "PM-KISAN திட்டம் தகுதியுள்ள சிறு மற்றும் குறு விவசாயிகளுக்கு ஆண்டுக்கு ₹6,000 வருமான ஆதரவு வழங்குகிறது. இந்த தொகை மூன்று தவணைகளில் நேரடியாக அவர்களின் வங்கிக் கணக்குகளில் செலுத்தப்படும். இந்தத் திட்டம் 2019 பிப்ரவரியில் அறிவிக்கப்பட்டு, 2018 டிசம்பரிலிருந்து நடைமுறையில் உள்ளது. விவசாயிகள் பொதுசேவை மையங்களை (CSC) அணுகி, நில உடைமை ஆவணங்கள், வங்கிக்கணக்குப் புத்தக நகல், ஆதார் நகல் மற்றும் குடும்ப அட்டை உள்ளிட்ட ஆவணங்களுடன் விண்ணப்பிக்க வேண்டும். விவரங்கள், தகுதி அல்லது விண்ணப்ப விவரங்கள் வேண்டுமா?"
            },
            "ask_pm_kisan_details": {
                "english": "The PM-KISAN scheme provides ₹6,000 per year (₹2,000 every 4 months) to small and marginal farmers to support farm expenses. It’s a direct benefit transfer scheme, credited to bank accounts. Benefits: financial stability and investment in farming. Interested in eligibility or documents?",
                "tamil": "PM-KISAN திட்டம் சிறு மற்றும் குறு விவசாயிகளுக்கு ஆண்டுக்கு ₹6,000 (ஒவ்வொரு 4 மாதங்களுக்கு ₹2,000) பண்ணை செலவுகளுக்கு ஆதரவாக வழங்குகிறது. இது வங்கி கணக்குகளுக்கு நேரடி பயன் பரிமாற்ற திட்டமாகும். பயன்கள்: நிதி ஸ்திரத்தன்மை மற்றும் விவசாயத்தில் முதலீடு. தகுதி அல்லது ஆவணங்கள் பற்றி அறிய வேண்டுமா?"
            },
            "ask_pm_kisan_eligibility": {
            "english": "The PM-KISAN scheme is open to all landholding farmer families in India, except for institutional landowners, professionals like doctors or engineers, and government employees or income tax payers. Eligibility mainly depends on ownership of cultivable land. A family includes husband, wife, and minor children. Need document or application details?",
             "tamil": "PM-KISAN திட்டம், நிறுவன நில உரிமையாளர்கள், தொழில்முறை நிபுணர்கள் (மருத்துவர்கள், பொறியாளர்கள்), அரசு ஊழியர்கள் மற்றும் வருமானவரி செலுத்துவோரைக் தவிர்த்து, இந்தியாவில் உள்ள அனைத்து நில உரிமையாளர் விவசாய குடும்பங்களுக்கும் திறந்துள்ளது. தகுதி பெரும்பாலும் சாகுபடி செய்யக்கூடிய நில உரிமையைப் பொறுத்தது. ஒரு குடும்பம் என்பது கணவன், மனைவி மற்றும் 18 வயதுக்குட்பட்ட குழந்தைகள் என வரையறுக்கப்படுகிறது. ஆவணங்கள் அல்லது விண்ணப்ப விவரங்கள் வேண்டுமா?"
            },

          "ask_pm_kisan_documents": {
          "english": "To apply for PM-KISAN, you need Aadhaar, proof of citizenship (like voter ID or passport), land ownership documents, and bank account details including IFSC. You can register via the PM-Kisan website or at Common Service Centres (CSCs). Want help with the application steps?",
           "tamil": "PM-KISAN திட்டத்தில் பதிவு செய்ய, ஆதார், குடியுரிமை சான்று (பாஸ்போர்ட், வாக்காளர் ஐடி போன்றவை), நில உரிமை ஆவணங்கள் மற்றும் வங்கி கணக்கு விவரங்கள் (IFSC உட்பட) தேவை. PM-Kisan வலைத்தளம் அல்லது பொது சேவை மையங்கள் (CSC) வாயிலாக நீங்கள் பதிவு செய்யலாம். விண்ணப்பிக்கும் படிகளை அறிய உதவ வேண்டுமா?"
          }
          ,
            "ask_pm_kisan_apply": {
                "english": "Apply through the PM-KISAN portal at https://pmkisan.gov.in or https://www.myscheme.gov.in/ or local agriculture office. Need steps?",
                "tamil": "PM-KISAN இணையதளத்தில் https://pmkisan.gov.in அல்லது https://www.myscheme.gov.in/ அல்லது உள்ளூர் வேளாண்மை அலுவலகம் மூலம் விண்ணப்பிக்கவும். படிகள் வேண்டுமா?"
            }
        }

        response = responses.get(intent, {}).get(language, "Sorry, I don't have information on that. Can you clarify?")
        dispatcher.utter_message(text=response)
        return []

class ActionSetLanguage(Action):
    def name(self) -> Text:
        return "action_set_language"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message.get('text', '').lower()
        print(f"User said: {user_message}")

        if "tamil" in user_message or "தமிழ்" in user_message:
            language = "tamil"
            msg = "மொழி வெற்றிகரமாக தமிழுக்கு மாற்றப்பட்டது."
        elif "english" in user_message or "ஆங்கிலம்" in user_message:
            language = "english"
            msg = "Language successfully switched to English."
        else:
            language = "english"  # default
            msg = "Language set to English. How can I assist you now?"

        dispatcher.utter_message(text=msg)
        return [SlotSet("language", language)]
