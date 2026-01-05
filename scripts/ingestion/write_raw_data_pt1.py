
import os

file_path = "data/raw/cloud_infrastructure_map_raw.txt"
os.makedirs(os.path.dirname(file_path), exist_ok=True)

part1 = """Cloud Regions
Metro Area
Cloud Service Provider, Cloud Region

Buenos Aires
Argentina
Huawei Cloud, LA Buenos Aires1 Zones
sa-argentina-1
Canberra
Australia
Microsoft Azure, Australia Central (Canberra)1 Zones
australiacentral
Microsoft Azure, Australia Central 2 (Canberra)1 Zones
australiacentral2
Oracle Cloud, Australian Gov (Canberra)1 Zones
au-gov-canberra-1
Melbourne
Australia
Amazon Web Services, Asia Pacific (Melbourne)3 Zones
ap-southeast-4
Google Cloud, Melbourne3 Zones
australia-southeast2
Microsoft Azure, Australia Southeast (Melbourne)1 Zones
australiasoutheast
Oracle Cloud, Australia Southeast (Melbourne)1 Zones
ap-melbourne-1
Sydney
Australia
Amazon Web Services, Asia Pacific (Sydney)3 Zones
ap-southeast-2
Google Cloud, Sydney3 Zones
australia-southeast1
IBM Cloud, Sydney3 Zones
au-syd
Microsoft Azure, Australia East (Sydney)3 Zones
australiaeast
Oracle Cloud, Australia East (Sydney)1 Zones
ap-sydney-1
OVH, Australia (Sydney)1 Zones
Vienna
Austria
Microsoft Azure, Austria East (Vienna)3 Zones
austriaeast
Manama
Bahrain
Amazon Web Services, Middle East (Bahrain)3 Zones
me-south-1
Brussels
Belgium
Microsoft Azure, Belgium Central3 ZonesPlanned
belgiumcentral
Mons
Belgium
Google Cloud, Belgium3 Zones
europe-west1
Campinas
Brazil
Oracle Cloud, Brazil Southeast (Vinhedo)1 Zones
sa-vinhedo-1
Rio de Janeiro
Brazil
Microsoft Azure, Brazil Southeast (Rio)3 Zones
brazilsoutheast
São Paulo
Brazil
Amazon Web Services, South America (São Paulo)3 Zones
sa-east-1
Google Cloud, Sao Paulo3 Zones
southamerica-east1
Huawei Cloud, LA-Sao Paulo3 Zones
sa-brazil-1
IBM Cloud, São Paulo3 Zones
br-sao
Microsoft Azure, Brazil South (São Paulo)3 Zones
brazilsouth
Oracle Cloud, Brazil East (Sao Paulo)1 Zones
sa-saopaulo-1
Tencent Cloud, South America (Sao Paulo)1 Zones
sl-saopaulo
Calgary
Canada
Amazon Web Services, Canada (West) 3 Zones
ca-west-1
Montréal
Canada
Amazon Web Services, Canada (Central)3 Zones
ca-central-1
Google Cloud, Montreal3 Zones
northamerica-northeast1
IBM Cloud, Montreal3 Zones
ca-mon
Oracle Cloud, Canada Southeast (Montreal)1 Zones
ca-montreal-1
OVH, East Coast (Montreal)1 Zones
Quebec City
Canada
Microsoft Azure, Canada East (Quebec City)1 Zones
canadaeast
Toronto
Canada
Google Cloud, Toronto3 Zones
northamerica-northeast2
IBM Cloud, Toronto3 Zones
ca-tor
Microsoft Azure, Canada Central (Toronto)3 Zones
canadacentral
Oracle Cloud, Canada Southeast (Toronto)1 Zones
ca-toronto-1
OVH, Canada (Toronto)1 Zones
Tencent Cloud, North America (Toronto)1 Zones
na-toronto
Santiago
Chile
Amazon Web Services, AWS Chile (Santiago)3 ZonesPlanned
Google Cloud, Santiago3 Zones
southamerica-west1
Huawei Cloud, LA-Santiago2 Zones
la-south-2
Microsoft Azure, Chile Central (Santiago)3 Zones
chilecentral
Oracle Cloud, Chile Central (Santiago)1 Zones
sa-santiago-1
Valparaíso
Chile
Oracle Cloud, Chile West (Vaparaíso)1 Zones
sa-valparaiso-1
Beijing
China
Alibaba Cloud, China North 2 (Beijing)12 Zones
cn-beijing
Amazon Web Services, Mainland China (Beijing)3 Zones
cn-north-1
Huawei Cloud, CN North Beijing13 Zones
cn-north-1
Huawei Cloud, CN North Beijing22 Zones
cn-north-2
Huawei Cloud, CN North Beijing32 Zones
cn-north-4
Microsoft Azure, China North (Beijing)1 Zones
chinanorth
Microsoft Azure, China North 2 (Beijing)1 Zones
chinanorth2
Microsoft Azure, China North 3 (Beijing)3 Zones
chinanorth3
Tencent Cloud, North China (Beijing)10 Zones
ap-beijing
Chengdu
China
Alibaba Cloud, China West 1 (Chengdu)2 Zones
cn-chengdu
Tencent Cloud, Southwest China (Chengdu)2 Zones
ap-chengdu
Chongqing
China
Tencent Cloud, Southwest China (Chongqing)1 Zones
ap-chongqing
Fuzhou
China
Alibaba Cloud, China (Fuzhou - Local Region)1 Zones
cn-fuzhou
Guangzhou
China
Alibaba Cloud, China South 3 (Guangzhou)2 Zones
cn-guangzhou
Huawei Cloud, CN South Guangzhou6 Zones
cn-south-1
Tencent Cloud, South China (Guangzhou)5 Zones
ap-guangzhou
Guiyang
China
Huawei Cloud, CN Southwest Guiyang3 Zones
cn-southwest-2
Hangzhou
China
Alibaba Cloud, China East 1 (Hangzhou)8 Zones
cn-hangzhou
Heyuan
China
Alibaba Cloud, China South 2 (Heyuan)2 Zones
cn-heyuan
Hong Kong
China
Alibaba Cloud, China (Hong Kong)3 Zones
cn-hongkong
Amazon Web Services, China (Hong Kong)3 Zones
ap-east-1
Google Cloud, Hong Kong3 Zones
asia-east2
Huawei Cloud, CN-Hong Kong4 Zones
ap-southeast-1
Microsoft Azure, East Asia (Hong Kong)3 Zones
eastasia
Tencent Cloud, Hong Kong3 Zones
ap-hongkong
Huhehaote
China
Alibaba Cloud, China North 5 (Hohhot)2 Zones
cn-huhehaote
Karamay
China
Huawei Cloud, CN Northwest Karamay1 Zones
cn-northwest-1
Nanjing
China
Alibaba Cloud, China East 3 (Nanjing)1 Zones
cn-nanjing
Microsoft Azure, China East 3 (Jiangsu)1 Zones
chinaeast3
Tencent Cloud, East China (Nanjing)3 Zones
ap-nanjing
Ningxiang
China
Amazon Web Services, Mainland China (Ningxia)3 Zones
cn-northwest-1
Qingdao
China
Alibaba Cloud, China North 1 (Qingdao)2 Zones
cn-qingdao
Shanghai
China
Alibaba Cloud, China East 2 (Shanghai)11 Zones
cn-shanghai
Huawei Cloud, CN East Shanghai14 Zones
cn-east-3
Huawei Cloud, CN East Shanghai24 Zones
cn-east-2
Microsoft Azure, China East (Shanghai)1 Zones
chinaeast
Microsoft Azure, China East 2 (Shanghai)1 Zones
chinaeast2
Tencent Cloud, East China (Shanghai)9 Zones
ap-shanghai
Shenzhen
China
Alibaba Cloud, China South 1 (Shenzhen)6 Zones
cn-shenzhen
Huawei Cloud, CN South Shenzhen1 Zones
cn-south-2
Tencent Cloud, South China (Shenzen) 3 Zones
ap-shenzhen
Ulanqab
China
Alibaba Cloud, China (Ulanqab)3 Zones
cn-ulanqab
Huawei Cloud, CN North Ulanqab1 3 Zones
cn-north-9
Wuhan
China
Alibaba Cloud, China (Wuhan - Local Region)1 Zones
cn-wuhan
Wuhu
China
Huawei Cloud, Huawei Cloud East China (Wuhu)3 Zones
Zhangjiakou
China
Alibaba Cloud, China North 3 (Zhangjiakou)3 Zones
cn-zhangjiakou
Bogotá
Colombia
Oracle Cloud, Colombia Central (Bogota)1 Zones
sa-bogota-1
Copenhagen
Denmark
Microsoft Azure, Denmark East (Copenhagen)3 ZonesPlanned
denmarkeast
Cairo
Egypt
Huawei Cloud, Huawei Cloud North Africa (Cairo)1 Zones
Hamina
Finland
Google Cloud, Finland3 Zones
europe-north1
Helsinki
Finland
Microsoft Azure, Finland (Helsinki)3 ZonesPlanned
finlandcentral
Dunkerque
France
OVH, France (Gravelines)1 Zones
Lille
France
OVH, Western Europe (Roubaix)1 Zones
Marseille
France
Microsoft Azure, France South (Marseille)1 Zones
francesouth
Oracle Cloud, France (Marseille)1 Zones
eu-marseille-1
Paris
France
Amazon Web Services, Europe West (Paris)3 Zones
eu-west-3
Google Cloud, Paris3 Zones
europe-west9
Microsoft Azure, France Central (Paris)3 Zones
francecentral
Oracle Cloud, France Central (Paris)1 Zones
eu-paris-1
OVH, Western Europe (Paris)3 Zones
Strasbourg
France
OVH, Western Europe (Strasbourg)1 Zones
Berlin
Germany
Google Cloud, Berlin3 Zones
europe-west10
Microsoft Azure, Germany North (Berlin)1 Zones
germanynorth
Frankfurt
Germany
Alibaba Cloud, EU Central 1 (Frankfurt)3 Zones
eu-central-1
Amazon Web Services, Europe Central (Frankfurt)3 Zones
eu-central-1
Amazon Web Services, European Sovereign Cloud (Germany)3 ZonesPlanned
Google Cloud, Frankfurt3 Zones
europe-west3
IBM Cloud, Frankfurt3 Zones
eu-de
Microsoft Azure, Germany West Central (Frankfurt)3 Zones
germanywestcentral
Oracle Cloud, EU Sovereign Central (Frankfurt)1 Zones
eu-sov-frankfurt-1
Oracle Cloud, Germany Central (Frankfurt)3 Zones
eu-frankfurt-1
OVH, Central Europe (Frankfurt)1 Zones
Tencent Cloud, Central Europe (Frankfurt)2 Zones
eu-frankfurt
Athens
Greece
Microsoft Azure, Greece Central (Athens)3 ZonesPlanned
greececentral
Chennai
India
Microsoft Azure, South India (Chennai)1 Zones
southindia
Hyderabad
India
Amazon Web Services, Asia Pacific (Hyderabad)3 Zones
ap-south-2
Microsoft Azure, Southcentral (Hyderabad)3 ZonesPlanned
indiasouthcentral
Oracle Cloud, India South (Hyderabad)1 Zones
ap-hyderabad-1
Mumbai
India
Amazon Web Services, Asia Pacific (Mumbai)3 Zones
ap-south-1
Google Cloud, Mumbai3 Zones
asia-south1
Microsoft Azure, West India (Mumbai)1 Zones
westindia
Oracle Cloud, India West (Mumbai)1 Zones
ap-mumbai-1
OVH, India (Mumbai)1 Zones
Tencent Cloud, South Asia (Mumbai)2 Zones
ap-mumbai
New Delhi
India
Google Cloud, Delhi3 Zones
asia-south2
Pune
India
Microsoft Azure, Central India (Pune)3 Zones
centralindia
Batam
Indonesia
Oracle Cloud, Indonesia North (Batam)1 Zones
Jakarta
Indonesia
Alibaba Cloud, Asia Pacific SE 5 (Jakarta)3 Zones
ap-southeast-5
Amazon Web Services, Indonesia (Jakarta)3 Zones
ap-southeast-3
Google Cloud, Jakarta3 Zones
asia-southeast2
Huawei Cloud, AP Jakarta3 Zones
ap-southeast-4
Microsoft Azure, Indonesia Central (Jakarta)3 Zones
indonesiacentral
Tencent Cloud, Southeast Asia Pacific (Jakarta)2 Zones
ap-jakarta
Dublin
Ireland
Amazon Web Services, Europe West (Ireland)3 Zones
eu-west-1
Huawei Cloud, EU Dublin2 Zones
eu-west-101
Microsoft Azure, North Europe (Dublin)3 Zones
northeurope
Jerusalem
Israel
Oracle Cloud, Israel Central (Jerusalem)1 Zones
il-jerusalem-1
Tel Aviv
Israel
Amazon Web Services, Middle East (Tel Aviv)3 Zones
il-central-1
Google Cloud, Tel Aviv3 Zones
me-west1
Microsoft Azure, Israel Central (Tel Aviv)3 Zones
israelcentral
Oracle Cloud, Israel 2 (Tel Aviv)1 ZonesPlanned
Milan
Italy
Amazon Web Services, Europe (Milan)3 Zones
eu-south-1
Google Cloud, Milan3 Zones
europe-west8
Microsoft Azure, Italy North (Milan)3 Zones
italynorth
Oracle Cloud, Italy Northwest (Milan)1 Zones
eu-milan-1
Turin
Italy
Google Cloud, Turin3 Zones
europe-west12
Oracle Cloud, Italy 2 (Turin)1 ZonesPlanned
Osaka
Japan
Amazon Web Services, Asia Pacific (Osaka)3 Zones
ap-northeast-3
Google Cloud, Osaka3 Zones
asia-northeast2
IBM Cloud, Osaka3 Zones
jp-osa
Microsoft Azure, Japan West (Osaka)1 Zones
japanwest
Oracle Cloud, Japan Central (Osaka)1 Zones
ap-osaka-1
Tencent Cloud, Northeast Asia Pacific 2 (Osaka)1 ZonesPlanned
Tokyo
Japan
Alibaba Cloud, Asia Pacific NE 1 (Tokyo)3 Zones
ap-northeast-1
Amazon Web Services, Asia Pacific (Tokyo)4 Zones
ap-northeast-1
Google Cloud, Tokyo3 Zones
asia-northeast1
IBM Cloud, Tokyo3 Zones
jp-tok
Microsoft Azure, Japan East (Saitama, Tokyo)3 Zones
japaneast
Oracle Cloud, Japan East (Tokyo)1 Zones
ap-tokyo-1
Tencent Cloud, Northeast Asia Pacific (Tokyo)2 Zones
ap-tokyo
Nairobi
Kenya
Microsoft Azure, East Africa (Nairobi)3 ZonesPlanned
Oracle Cloud, Kenya (Nairobi)1 ZonesPlanned
Kuala Lumpur
Malaysia
Alibaba Cloud, Asia Pacific SE 3 (Kuala Lumpur)3 Zones
ap-southeast-3
Amazon Web Services, Malaysia3 Zones
Microsoft Azure, Malaysia West (Kuala Lumpur)3 Zones
malaysiawest
Oracle Cloud, Malaysia1 ZonesPlanned
Mexico City
Mexico
Huawei Cloud, LA-Mexico City12 Zones
na-mexico-1
Huawei Cloud, LA-Mexico City22 Zones
la-north-2
Monterrey
Mexico
Oracle Cloud, Mexico Northeast (Monterrey)1 Zones
mx-monterrey-1
Santiago de Querétaro
Mexico
Alibaba Cloud, Mexico (Querétaro)1 Zones
Amazon Web Services, AWS Mexico central3 Zones
Google Cloud, Mexico3 Zones
Microsoft Azure, Mexico Central (Querétaro)3 Zones
mexicocentral
Oracle Cloud, Mexico Central (Querétaro)1 Zones
mx-queretaro-1
Casablanca
Morocco
Oracle Cloud, Morocco 1 (Casablanca)1 ZonesPlanned
Settat
Morocco
Oracle Cloud, Morocco 2 (Settat)1 ZonesPlanned
Amsterdam
Netherlands
Microsoft Azure, West Europe (Amsterdam)3 Zones
westeurope
Oracle Cloud, Netherlands Northwest (Amsterdam)1 Zones
eu-amsterdam-1
Groningen
Netherlands
Google Cloud, Netherlands3 Zones
europe-west4
Auckland
New Zealand
Amazon Web Services, Asia Pacific (Auckland)3 Zones
ap-east-2
Google Cloud, New Zealand3 ZonesPlanned
Microsoft Azure, New Zealand North (Auckland)3 Zones
newzealandnorth
Oslo
Norway
Google Cloud, Norway3 ZonesPlanned
Microsoft Azure, Norway East (Oslo)3 Zones
norwayeast
Stavanger
Norway
Microsoft Azure, Norway West (Stavanger)1 Zones
norwaywest
Lima
Peru
Huawei Cloud, LA-Lima12 Zones
sa-peru-1
Manila
Philippines
Alibaba Cloud, Asia Pacific SE 6 (Manila)2 Zones
ap-southeast-6
Huawei Cloud, AP-Manila3 Zones
Sochaczew
Poland
OVH, Western Europe 1 Zones
Warsaw
Poland
Google Cloud, Warsaw3 Zones
europe-central2
Microsoft Azure, Poland Central (Warsaw)3 Zones
polandcentral
OVH, Central Europe (Warsaw)1 Zones
Doha
Qatar
Google Cloud, Doha3 Zones
me-central1
Microsoft Azure, Qatar Central (Doha)3 Zones
qatarcentral
Dammam
Saudi Arabia
Google Cloud, Damman3 Zones
me-central2
Jeddah
Saudi Arabia
Oracle Cloud, Saudi Arabia West (Jeddah)1 Zones
me-jeddah-1
Riyadh
Saudi Arabia
Alibaba Cloud, Saudi Arabia (Riyadh)2 Zones
me-east-1
Amazon Web Services, Saudi Arabia (Riyadh)3 ZonesPlanned
Huawei Cloud, ME Riyadh3 Zones
me-east-1
Microsoft Azure, Saudi Arabia East3 ZonesPlanned
saudiarabiasouthcentral
Oracle Cloud, Saudi Arabia 31 ZonesPlanned
Oracle Cloud, Saudi Arabia Central (Riyadh)1 Zones
Tencent Cloud, Middle East (Riyadh)2 ZonesPlanned
Kragujevac
Serbia
Oracle Cloud, Serbia Central (Jovanovac)1 Zones
eu-jovanovac-1
Singapore
Singapore
Alibaba Cloud, Asia Pacific SE 1 (Singapore)3 Zones
ap-southeast-1
Amazon Web Services, Asia Pacific (Singapore)3 Zones
ap-southeast-1
Google Cloud, Singapore3 Zones
asia-southeast1
Huawei Cloud, AP-Singapore4 Zones
ap-southeast-3
Microsoft Azure, Southeast Asia (Singapore)3 Zones
southeastasia
Oracle Cloud, Singapore (Singapore)2 Zones
ap-singapore-1
Oracle Cloud, Singapore West1 Zones
ap-singapore-2
OVH, Asia (Singapore)1 Zones
Tencent Cloud, Southeast Asia Pacific (Singapore)4 Zones
ap-singapore
Cape Town
South Africa
Amazon Web Services, Africa (Cape Town)3 Zones
af-south-1
Microsoft Azure, South Africa West (Cape Town)1 Zones
southafricawest
Johannesburg
South Africa
Google Cloud, Johannesburg3 Zones
africa-south1
Huawei Cloud, AF-Johannesburg3 Zones
af-south-1
Microsoft Azure, South Africa North (Johannesburg)3 Zones
southafricanorth
Oracle Cloud, South Africa Central(Johannesburg)1 Zones
af-johannesburg-1
Busan
South Korea
Microsoft Azure, Korea South (Busan)1 Zones
koreasouth
Chuncheon
South Korea
Oracle Cloud, South Korea North (Chuncheon)1 Zones
ap-chuncheon-1
Seoul
South Korea
Alibaba Cloud, Asia Pacific NE 2 (Seoul)2 Zones
ap-northeast-2
Amazon Web Services, Asia Pacific (Seoul)4 Zones
ap-northeast-2
Google Cloud, Seoul3 Zones
asia-northeast3
Microsoft Azure, Korea Central (Seoul)3 Zones
koreacentral
Oracle Cloud, South Korea Central (Seoul)1 Zones
ap-seoul-1
Tencent Cloud, Northeast Asia Pacific (Seoul)2 Zones
ap-seoul
Madrid
Spain
Google Cloud, Madrid3 Zones
europe-southwest1
IBM Cloud, Madrid3 Zones
eu-sp
Microsoft Azure, Spain Central (Madrid)3 Zones
spaincentral
Oracle Cloud, EU Sovereign South (Madrid)1 Zones
eu-sov-madrid-1
Oracle Cloud, Spain Central (Madrid)1 Zones
eu-madrid-1
Oracle Cloud, Spain Central (Madrid)1 ZonesPlanned
Zaragoza
Spain
Amazon Web Services, Europe South (Spain)3 Zones
eu-south-2
Gävle
Sweden
Microsoft Azure, Sweden Central (Gävle)3 Zones
swedencentral
Malmö
Sweden
Microsoft Azure, Sweden South (Staffanstorp)3 Zones
swedensouth
Stockholm
Sweden
Amazon Web Services, Europe North (Stockholm)3 Zones
eu-north-1
Google Cloud, Sweden3 Zones
europe-north2
Oracle Cloud, Sweden Central (Stockholm)1 Zones
eu-stockholm-1
Geneva
Switzerland
Microsoft Azure, Switzerland West (Geneva)1 Zones
switzerlandwest
Zürich
Switzerland
Amazon Web Services, Europe (Zurich) 3 Zones
eu-central-2
Google Cloud, Zurich3 Zones
europe-west6
Microsoft Azure, Switzerland North (Zürich)1 Zones
switzerlandnorth
Oracle Cloud, Switzerland North (Zurich)1 Zones
eu-zurich-1
Taichung
Taiwan
Google Cloud, Taiwan3 Zones
asia-east1
Taipei
Taiwan
Amazon Web Services, Asia Pacific (Taipei)3 Zones
Microsoft Azure, Taiwan North (Taipei)3 ZonesPlanned
taiwannorth
Bangkok
Thailand
Alibaba Cloud, Asia Pacific SE 7 (Bangkok)1 Zones
ap-southeast-7
Amazon Web Services, AWS Thailand3 Zones
ap-southeast-7
Google Cloud, Thailand3 ZonesPlanned
Huawei Cloud, AP-Bangkok3 Zones
ap-southeast-2
Microsoft Azure, Thailand3 ZonesPlanned
Tencent Cloud, Southeast Asia (Bangkok)2 Zones
ap-bangkok
Istanbul
Turkey
Huawei Cloud, TR-Istanbul3 Zones
tr-west-1
Abu Dhabi
United Arab Emirates
Microsoft Azure, UAE Central (Abu Dhabi)1 Zones
uaecentral
Oracle Cloud, United Arab Emirates (Abu Dhabi)1 Zones
me-abudhabi-1
Dubai
United Arab Emirates
Alibaba Cloud, Middle East 1 (Dubai)1 Zones
me-east-1
Amazon Web Services, United Arab Emirates3 Zones
me-central-1
Microsoft Azure, UAE North (Dubai)3 Zones
uaenorth
Oracle Cloud, United Arab Emirates (Dubai)1 Zones
me-dubai-1
Cardiff
United Kingdom
Microsoft Azure, UK West (Cardiff)1 Zones
ukwest
London
United Kingdom
Alibaba Cloud, UK (London)2 Zones
eu-west-1
Amazon Web Services, Europe West (London)3 Zones
eu-west-2
Google Cloud, London3 Zones
europe-west2
IBM Cloud, London3 Zones
eu-gb
Microsoft Azure, UK South (London)3 Zones
uksouth
Oracle Cloud, UK Gov South (London)1 Zones
uk-gov-london-1
Oracle Cloud, UK South (London)3 Zones
uk-london-1
OVH, Western Europe (London)1 Zones
Newport
United Kingdom
Oracle Cloud, UK Gov West (Newport)1 Zones
uk-gov-newport-1
Oracle Cloud, UK West (Newport)1 Zones
uk-cardiff-1
Atlanta
United States
Microsoft Azure, East US 3 (Atlanta)3 ZonesPlanned
eastus3
Austin
United States
Microsoft Azure, US Gov Texas1 Zones
usgovtexas
Charleston
United States
Google Cloud, South Carolina3 Zones
us-east1
Cheyenne
United States
Microsoft Azure, West Central US (Cheyenne)3 Zones
westcentralus
Chicago
United States
Microsoft Azure, North Central US (Chicago)1 Zones
northcentralus
Oracle Cloud, US DoD North1 Zones
us-gov-chicago-1
Oracle Cloud, US Midwest (Chicago)1 Zones
us-chicago-1
Columbus
United States
Amazon Web Services, AWS GovCloud (US-East)3 Zones
us-gov-east-1
Amazon Web Services, US East (Ohio)3 Zones
us-east-2
Google Cloud, Columbus3 Zones
us-east5
Dallas
United States
Google Cloud, Dallas3 Zones
us-south1
IBM Cloud, Dallas3 Zones
us-south
Des Moines
United States
Microsoft Azure, Central US (Des Moines)3 Zones
centralus
Microsoft Azure, US DoD Central1 Zones
usdodwest
Microsoft Azure, US Sec West Central3 Zones
Hermiston
United States
Amazon Web Services, AWS GovCloud (US-West)3 Zones
us-gov-west-1
Amazon Web Services, US West (Oregon)4 Zones
us-west-1
Las Vegas
United States
Google Cloud, Las Vegas3 Zones
us-west4
Los Angeles
United States
Google Cloud, Los Angeles3 Zones
us-west2
Moses Lake
United States
Microsoft Azure, West US 2 (Quincy)3 Zones
westus2
Omaha
United States
Google Cloud, Iowa4 Zones
us-central1
Phoenix
United States
Google Cloud, Phoenix3 ZonesPlanned
Microsoft Azure, US Gov Arizona1 Zones
usgovarizona
Microsoft Azure, West US 3 (Phoenix)3 Zones
westus3
Oracle Cloud, US DoD West1 Zones
us-gov-phoenix-1
Oracle Cloud, US Gov West (Phoenix)1 Zones
us-luke-1
Oracle Cloud, US West (Phoenix)3 Zones
us-phoenix-1
Portland
United States
OVH, West Coast (Seattle)1 Zones
Richmond
United States
Microsoft Azure, East US (Richmond)3 Zones
eastus
Microsoft Azure, East US 2 (Richmond)3 Zones
eastus2
Microsoft Azure, US DoD East1 Zones
usdodeast
Microsoft Azure, US Sec East1 Zones
usseceast
Salt Lake City
United States
Google Cloud, Salt Lake City3 Zones
us-west3
San Antonio
United States
Microsoft Azure, South Central US (San Antonio)3 Zones
southcentralus
San Francisco
United States
Alibaba Cloud, US West 1 (Silicon Valley)2 Zones
us-west-1
Amazon Web Services, US West (Northern California)3 Zones
us-west-2
Microsoft Azure, US Sec West1 Zones
ussecwest
Microsoft Azure, West US (San Francisco)1 Zones
westus
Oracle Cloud, US West (San Jose)1 Zones
us-sanjose-1
Tencent Cloud, Western U.S. (Silicon Valley)2 Zones
na-siliconvalley
The Dalles
United States
Google Cloud, Oregon3 Zones
us-west1
Washington
United States
Alibaba Cloud, US East 1 (Virginia)2 Zones
us-east-1
Amazon Web Services, US East (Northern Virginia)6 Zones
us-east-1
Google Cloud, Northern Virginia3 Zones
us-east4
IBM Cloud, Washington DC3 Zones
us-east
Microsoft Azure, US Gov Virginia 3 Zones
usgovvirginia
Oracle Cloud, US DoD East1 Zones
us-ashburn-1
Oracle Cloud, US East (Ashburn)3 Zones
us-ashburn-1
Oracle Cloud, US Gov East (Ashburn)1 Zones
us-langley-1
OVH, East Coast (Washington DC)1 Zones
Tencent Cloud, Eastern U.S. (Virginia)2 Zones
na-ashburn
"""

with open(file_path, "w", encoding="utf-8") as f:
    f.write(part1)

print(f"Part 1 wrote {len(part1)} characters.")
