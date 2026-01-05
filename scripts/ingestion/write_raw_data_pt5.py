
file_path = "data/raw/cloud_infrastructure_map_raw.txt"

part5 = """
Tokyo
Japan
Amazon Web Services, Equinix TY10, Equinix
2-2-19 Edagawa, Koto-ku, Tokyo, Japan
Amazon Web Services, Equinix TY2, Equinix
1-9-20 Higashi-Shinagawa, Shinagawa-ku, Tokyo, Japan
Amazon Web Services, Equinix TY4, Equinix
1-3-7 Otemachi, Chiyoda-ku, Tokyo, Japan
Amazon Web Services, IIJ Cool Shiroi Data Center, IIJ
Shiroi-shi, Chiba, Tokyo, Japan
Google Cloud, @Tokyo CC1, @Tokyo
5-6-36 Toyosa, Koto-ku, Tokyo, Japan
Google Cloud, Equinix TY2, Equinix
1-9-20 Higashi-Shinagawa, Shinagawa-ku, Tokyo, Japan
Google Cloud, Equinix TY4, Equinix
1-3-7 Otemachi, Chiyoda-ku, Tokyo, Japan
Google Cloud, NTTData Com Otemachi, NTT Data
Chiyoda-ku, Tokyo, Japan
IBM Cloud, Equinix TY2, Equinix
1-9-20 Higashi-Shinagawa, Shinagawa-ku, Tokyo, Japan
IBM Cloud, Equinix TY3, Equinix
1-2-16 Ariake, Koto-ku, Tokyo, Japan
IBM Cloud, Equinix TY4, Equinix
1-3-7 Otemachi, Chiyoda-ku, Tokyo, Japan
IBM Cloud, IBM Tokyo (Makuhari), IBM
1-1 Nakase, Mihama-ku, Tokyo, Japan
Microsoft Azure, @Tokyo CC1, @Tokyo
5-6-36 Toyosa, Koto-ku, Tokyo, Japan
Microsoft Azure, Colt Tokyo Shiohama, Colt
2-10-1 Shiohama, Koto-ku, Tokyo, Japan
Microsoft Azure, Equinix TY4, Equinix
1-3-7 Otemachi, Chiyoda-ku, Tokyo, Japan
Oracle Cloud, Equinix TY4, Equinix
1-3-7 Otemachi, Chiyoda-ku, Tokyo, Japan
Oracle Cloud, NTTData Com Otemachi, NTT Data
Chiyoda-ku, Tokyo, Japan
Tencent Cloud, ap-tokyo-1, Tencent Cloud
Tokyo, Japan
Tencent Cloud, ap-tokyo-2, Tencent Cloud
Tokyo, Japan
Tencent Cloud, Equinix TY8, Equinix
1-9-20 Higashi-Shinagawa, Shinagawa-ku, Tokyo, Japan
Nairobi
Kenya
Google Cloud, IXAfrica NBO1, IXAfrica
Nairobi, Kenya
Oracle Cloud, iColo.io NBO1, iColo.io
Mombasa Road, Nairobi, Kenya
Kuala Lumpur
Malaysia
Alibaba Cloud, Kul-A, VNET
Kuala Lumpur, Malaysia
Alibaba Cloud, Kul-B, TM ONE
Kuala Lumpur, Malaysia
Alibaba Cloud, Kul-C, TIME dotcom
Kuala Lumpur, Malaysia
Microsoft Azure, AIMS Kuala Lumpur, AIMS
Menara AIMS, Kuala Lumpur, Malaysia
Microsoft Azure, Vantage KUL11, Vantage Data Centers
Cyberjaya, Kuala Lumpur, Malaysia
Mexico City
Mexico
Huawei Cloud, Elara Comunicaciones Mexico, Elara Comunicaciones
Mexico City, Mexico
Huawei Cloud, KIO Networks MEX 1, KIO Networks
Mexico City, Mexico
Huawei Cloud, KIO Networks MEX 2, KIO Networks
Mexico City, Mexico
Santiago de Querétaro
Mexico
Google Cloud, Equinix MX1, Equinix
Carretera Estatal 431, "El Colorado-Galindo' km 3+800, Santiago de Querétaro, Mexico
Google Cloud, Telmex Queretaro (Triara), Telmex
Santiago de Querétaro, Mexico
Microsoft Azure, KIO Networks QRO 1, KIO Networks
Santiago de Querétaro, Mexico
Oracle Cloud, Equinix MX1, Equinix
Carretera Estatal 431, "El Colorado-Galindo' km 3+800, Santiago de Querétaro, Mexico
Oracle Cloud, Telmex Queretaro (Triara), Telmex
Santiago de Querétaro, Mexico
Auckland
New Zealand
Amazon Web Services, Datacom Orbit, Datacom
16-18 Piermark Drive, Rosedale, Auckland, New Zealand
Microsoft Azure, Datacom Orbit, Datacom
16-18 Piermark Drive, Rosedale, Auckland, New Zealand
Lagos
Nigeria
Google Cloud, OADC Lagos, OADC
Lekki, Lagos, Nigeria
Oslo
Norway
Microsoft Azure, DigiPlex Ulven, DigiPlex
Ulvenveien 82-89, Oslo, Norway
Muscat
Oman
Amazon Web Services, Equinix MC1, Equinix
Muscat, Oman
Oracle Cloud, Datamount Jebel Akhdar, Datamount
Jebel Akhdar, Muscat, Indonesia
Manila
Philippines
Alibaba Cloud, ePLDT Vitro Makati, PLDT
Makati City, Manila, Philippines
Alibaba Cloud, Globe MK2, Globe
Makati City, Manila, Philippines
Google Cloud, ePLDT Vitro Makati, PLDT
Makati City, Manila, Philippines
Huawei Cloud, ePLDT Vitro Makati, PLDT
Makati City, Manila, Philippines
Huawei Cloud, ePLDT Vitro Pasig, PLDT
Pasig City, Manila, Philippines
Huawei Cloud, Globe MK2, Globe
Makati City, Manila, Philippines
Warsaw
Poland
Google Cloud, Equinix WA3, Equinix
Aleje Jerozolimskie, Warsaw, Poland
Google Cloud, Polcom Skawina, Polcom
Skawina, Warsaw, Poland
Microsoft Azure, Equinix WA3, Equinix
Aleje Jerozolimskie, Warsaw, Poland
Lisbon
Portugal
Google Cloud, Equinix LS1, Equinix
Avenida Severiano Falcaol, Lisbon, Portugal
Doha
Qatar
Google Cloud, Meeza M-Vault 2, Meeza
Doha, Qatar
Google Cloud, Meeza M-Vault 3, Meeza
Doha, Qatar
Google Cloud, Ooredoo QDC5, Ooredoo
Mesaimeer, Doha, Qatar
Microsoft Azure, Ooredoo QDC5, Ooredoo
Mesaimeer, Doha, Qatar
Jeddah
Saudi Arabia
Oracle Cloud, Center3 Jeddah (MG1), Center3
Al Andalus 2623, Jeddah, Saudi Arabia
Riyadh
Saudi Arabia
Huawei Cloud, Center3 Riyadh (DC2), Center3
3291 Al Imam Saud Ibn Abdul Aziz Branch, Riyadh, Saudi Arabia
Huawei Cloud, Mobily Malga 2, Mobily
Riyadh, Saudi Arabia
Oracle Cloud, Center3 Riyadh (DC2), Center3
3291 Al Imam Saud Ibn Abdul Aziz Branch, Riyadh, Saudi Arabia
Singapore
Singapore
Alibaba Cloud, Digital Realty SIN11 (Jurong West), Digital Realty
36 Joo Koon Circle, Singapore, Singapore
Alibaba Cloud, Equinix SG2, Equinix
15 Pioneer Walk, Singapore, Singapore
Alibaba Cloud, Global Switch Singapore Tai Seng, Global Switch
2 Tai Seng Avenue, Singapore, Singapore
Amazon Web Services, Equinix SG2, Equinix
15 Pioneer Walk, Singapore, Singapore
Amazon Web Services, Global Switch Singapore Tai Seng, Global Switch
2 Tai Seng Avenue, Singapore, Singapore
Amazon Web Services, New Media Express (NME) Singapore, New Media Express
800 Upper Bukit Timah Road, Singapore, Singapore
Google Cloud, Equinix SG2, Equinix
15 Pioneer Walk, Singapore, Singapore
Google Cloud, Global Switch Singapore Tai Seng, Global Switch
2 Tai Seng Avenue, Singapore, Singapore
Huawei Cloud, Equinix SG2, Equinix
15 Pioneer Walk, Singapore, Singapore
Huawei Cloud, Global Switch Singapore Tai Seng, Global Switch
2 Tai Seng Avenue, Singapore, Singapore
Huawei Cloud, Telin Singapore 1, Telin Singapore
Changi North Way, Singapore, Singapore
Huawei Cloud, Telin Singapore 3, Telin Singapore
Tanjong Kling, Singapore, Singapore
Microsoft Azure, Equinix SG2, Equinix
15 Pioneer Walk, Singapore, Singapore
Microsoft Azure, Global Switch Singapore Tai Seng, Global Switch
2 Tai Seng Avenue, Singapore, Singapore
Oracle Cloud, Equinix SG3, Equinix
26A Ayer Rajah Crescent, Singapore, Singapore
Oracle Cloud, Global Switch Singapore Tai Seng, Global Switch
2 Tai Seng Avenue, Singapore, Singapore
Tencent Cloud, Equinix SG3, Equinix
26A Ayer Rajah Crescent, Singapore, Singapore
Tencent Cloud, Keppel DC Singapore 4, Keppel Data Centres
20 Tampines Street 92, Singapore, Singapore
Cape Town
South Africa
Amazon Web Services, Teraco CT1, Teraco Data Environments
260 Surrey Ave, Ferndale, Cape Town, South Africa
Microsoft Azure, Teraco CT1, Teraco Data Environments
260 Surrey Ave, Ferndale, Cape Town, South Africa
Johannesburg
South Africa
Amazon Web Services, Teraco JB1, Teraco Data Environments
18 Isando Road, Isando, Johannesburg, South Africa
Google Cloud, Africa Data Centres JHB1, Africa Data Centres
Die Hoewes, Centurion, Johannesburg, South Africa
Google Cloud, Teraco JB1, Teraco Data Environments
18 Isando Road, Isando, Johannesburg, South Africa
Huawei Cloud, BCX Centurion, BCX
Johannesburg, South Africa
Huawei Cloud, MTN Centurion , MTN
Johannesburg, South Africa
Huawei Cloud, Teraco JB1, Teraco Data Environments
18 Isando Road, Isando, Johannesburg, South Africa
Microsoft Azure, Teraco JB1, Teraco Data Environments
18 Isando Road, Isando, Johannesburg, South Africa
Oracle Cloud, Africa Data Centres JHB1, Africa Data Centres
Die Hoewes, Centurion, Johannesburg, South Africa
Oracle Cloud, Telkom Park (Centurion), Telkom
61 Oak Ave, Johannesburg, South Africa
Seoul
South Korea
Alibaba Cloud, SK Broadband Seocho, SK Broadband
Seoul, South Korea
Alibaba Cloud, SK Broadband Sheffield, SK Broadband
Seoul, South Korea
Amazon Web Services, KINX Gasan, KINX
Gasan, Seoul, South Korea
Amazon Web Services, LG U+ Pyeongchon Mega Center, LG U+
Pyeongchon, Seoul, South Korea
Amazon Web Services, Lotte Data Communication (LDCC) Gasan, Lotte Data Communication
150-1 Gasan-dong, Geumcheon-gu, Seoul, South Korea
Google Cloud, KINX Dogok, KINX
2624 Nambusunhwan-ro, Gangnam-gu, Seoul, South Korea
Google Cloud, LG U+ Pyeongchon Mega Center, LG U+
Pyeongchon, Seoul, South Korea
Google Cloud, Sejong Telecom Yeoksam, Sejong Telecom
Yeoksam, Seoul, South Korea
Microsoft Azure, KINX Dogok, KINX
2624 Nambusunhwan-ro, Gangnam-gu, Seoul, South Korea
Microsoft Azure, LG CNS Sangam IT Center, LG CNS
Sangam, Seoul, South Korea
Oracle Cloud, KINX Gasan, KINX
Gasan, Seoul, South Korea
Oracle Cloud, KT Mokdong 1 (IDC 1), KT
Mokdong, Seoul, South Korea
Tencent Cloud, Equinix SL1, Equinix
Samsung-ro, Seoul, South Korea
Tencent Cloud, LG U+ Pyeongchon Mega Center, LG U+
Pyeongchon, Seoul, South Korea
Madrid
Spain
Google Cloud, Digital Realty MAD1, Digital Realty
Calle de Cañada Real de las Merinas 15, Madrid, Spain
Google Cloud, Digital Realty MAD4, Digital Realty
Avenida de Bruselas 20, Madrid, Spain
Google Cloud, Global Switch Madrid, Global Switch
Calle de Yecora 4, Madrid, Spain
IBM Cloud, Digital Realty MAD4, Digital Realty
Avenida de Bruselas 20, Madrid, Spain
IBM Cloud, Equinix MD2, Equinix
Calle de Valgrande, 6, Alcobendas, Madrid, Spain
IBM Cloud, Global Switch Madrid, Global Switch
Calle de Yecora 4, Madrid, Spain
Microsoft Azure, Digital Realty MAD4, Digital Realty
Avenida de Bruselas 20, Madrid, Spain
Microsoft Azure, Equinix MD2, Equinix
Calle de Valgrande, 6, Alcobendas, Madrid, Spain
Oracle Cloud, Equinix MD2, Equinix
Calle de Valgrande, 6, Alcobendas, Madrid, Spain
Oracle Cloud, Global Switch Madrid, Global Switch
Calle de Yecora 4, Madrid, Spain
Stockholm
Sweden
Amazon Web Services, Equinix SK1, Equinix
Raukvaegen 3, Stockholm, Sweden
Amazon Web Services, Equinix SK2, Equinix
Esbogatan 11, Stockholm, Sweden
Amazon Web Services, Equinix SK3, Equinix
Västberga Allé 60, Stockholm, Sweden
Google Cloud, DigiPlex Stockholm, DigiPlex
Domnarvsgatan 11, Stockholm, Sweden
Google Cloud, Equinix SK1, Equinix
Raukvaegen 3, Stockholm, Sweden
Google Cloud, ObeHosting Kista Gate, ObeHosting
Torshamnsgatan 35-39, Kista, Stockholm, Sweden
Oracle Cloud, Equinix SK2, Equinix
Esbogatan 11, Stockholm, Sweden
Geneva
Switzerland
Microsoft Azure, Equinix GV2, Equinix
Rue de la Mairie, Geneva, Switzerland
Zürich
Switzerland
Amazon Web Services, Equinix ZH5, Equinix
Allmendstrasse 11-13, Zürich, Switzerland
Google Cloud, Equinix ZH4, Equinix
Josefstrasse 225, Zürich, Switzerland
Google Cloud, Green Zurich West 1 & 2, Green
Industriestrasse 33, Lupfig, Zürich, Switzerland
Google Cloud, Interxion ZUR1, Digital Realty
Sägereistrasse 35, Zürich, Switzerland
Microsoft Azure, Interxion ZUR1, Digital Realty
Sägereistrasse 35, Zürich, Switzerland
Oracle Cloud, Interxion ZUR1, Digital Realty
Sägereistrasse 35, Zürich, Switzerland
Taipei
Taiwan
Amazon Web Services, Chief Telecom LY, Chief Telecom
No. 216, Ruiguang Road, Neihu District, Taipei, Taiwan
Microsoft Azure, Chief Telecom LY, Chief Telecom
No. 216, Ruiguang Road, Neihu District, Taipei, Taiwan
Bangkok
Thailand
Alibaba Cloud, True IDC - North Muang Thong, True IDC
Bangkok, Thailand
Amazon Web Services, Equinix BKK1, Equinix
Bangna, Bangkok, Thailand
Huawei Cloud, CAT Tower - Bangrak, CAT
Bangna, Bangkok, Thailand
Huawei Cloud, CS Loxinfo The Cloud, CS Loxinfo
Bangna, Bangkok, Thailand
Huawei Cloud, TCCtech-Bna-Bangna, TCC Technology (TCCtech)
1854 Bangna-Trad Road, Bangna, Bangkok, Thailand
Tencent Cloud, True IDC - East Bangna, True IDC
Bangna, Bangkok, Thailand
Tencent Cloud, True IDC - North Muang Thong, True IDC
Bangkok, Thailand
Istanbul
Turkey
Huawei Cloud, Turkcell Gebze, Turkcell
Istanbul, Turkey
Huawei Cloud, Turkcell Kartal, Turkcell
Istanbul, Turkey
Dubai
United Arab Emirates
Alibaba Cloud, Moro Hub (Data Hub Integrated Solutions L.L.C), Moro Hub
Dubai, United Arab Emirates
Amazon Web Services, Equinix DX1, Equinix
Dubai, United Arab Emirates
Microsoft Azure, Equinix DX1, Equinix
Dubai, United Arab Emirates
Microsoft Azure, Ooredoo QDC5, Ooredoo
Mesaimeer, Doha, United Arab Emirates
Oracle Cloud, Equinix DX1, Equinix
Dubai, United Arab Emirates
London
United Kingdom
Alibaba Cloud, Equinix LD5, Equinix
8 Buckingham Avenue, Slough, London, United Kingdom
Alibaba Cloud, Global Switch London East, Global Switch
East India Dock House, 240 East India Dock Road, London, United Kingdom
Amazon Web Services, Equinix LD5, Equinix
8 Buckingham Avenue, Slough, London, United Kingdom
Amazon Web Services, TELEHOUSE London Docklands West, TELEHOUSE
14 Coriander Avenue, London, United Kingdom
Google Cloud, Equinix LD5, Equinix
8 Buckingham Avenue, Slough, London, United Kingdom
Google Cloud, Global Switch London North, Global Switch
East India Dock House, 240 East India Dock Road, London, United Kingdom
Google Cloud, TELEHOUSE London Docklands North, TELEHOUSE
14 Coriander Avenue, London, United Kingdom
IBM Cloud, CenturyLink London 3 (Slough), CenturyLink
210 Bath Road, Slough, London, United Kingdom
IBM Cloud, Equinix LD5, Equinix
8 Buckingham Avenue, Slough, London, United Kingdom
IBM Cloud, Global Switch London East, Global Switch
East India Dock House, 240 East India Dock Road, London, United Kingdom
Microsoft Azure, Cyxtera LHR1, Cyxtera
660-665 Ajax Avenue, Slough, London, United Kingdom
Microsoft Azure, Equinix LD5, Equinix
8 Buckingham Avenue, Slough, London, United Kingdom
Oracle Cloud, Equinix LD5, Equinix
8 Buckingham Avenue, Slough, London, United Kingdom
Oracle Cloud, Global Switch London East, Global Switch
East India Dock House, 240 East India Dock Road, London, United Kingdom
Manchester
United Kingdom
Microsoft Azure, Equinix MA1, Equinix
Reynolds House, 4 Lloyd Street North, Manchester, United Kingdom
Atlanta
United States
Amazon Web Services, Digital Realty ATL1, Digital Realty
56 Marietta Street, Atlanta, GA, United States
Amazon Web Services, Equinix AT2, Equinix
180 Peachtree Street NW, Atlanta, GA, United States
Google Cloud, Digital Realty ATL1, Digital Realty
56 Marietta Street, Atlanta, GA, United States
Google Cloud, Equinix AT1, Equinix
180 Peachtree Street NW, Atlanta, GA, United States
Google Cloud, QTS Atlanta-Metro, QTS
1033 Jefferson St NW, Atlanta, GA, United States
Microsoft Azure, Digital Realty ATL1, Digital Realty
56 Marietta Street, Atlanta, GA, United States
Microsoft Azure, Equinix AT2, Equinix
180 Peachtree Street NW, Atlanta, GA, United States
Boston
United States
Amazon Web Services, CoreSite BO1, CoreSite
70 Inner Belt Road, Somerville, MA, United States
Amazon Web Services, Markley 1 Summer, Markley Group
1 Summer Street, Boston, MA, United States
Chicago
United States
Amazon Web Services, Digital Realty CHI1, Digital Realty
350 East Cermak Road, Chicago, IL, United States
Amazon Web Services, Equinix CH1, Equinix
350 East Cermak Road, Chicago, IL, United States
Amazon Web Services, Equinix CH2, Equinix
350 East Cermak Road, Chicago, IL, United States
Microsoft Azure, Digital Realty CHI1, Digital Realty
350 East Cermak Road, Chicago, IL, United States
Microsoft Azure, Equinix CH1, Equinix
350 East Cermak Road, Chicago, IL, United States
Microsoft Azure, T5 Data Centers Chicago, T5 Data Centers
200 Innovation Boulevard, Elk Grove Village, Chicago, IL, United States
Oracle Cloud, Digital Realty CHI1, Digital Realty
350 East Cermak Road, Chicago, IL, United States
Oracle Cloud, Equinix CH3, Equinix
1431 Opus Place, Downers Grove, Chicago, IL, United States
Columbus
United States
Amazon Web Services, Cologix COL3, Cologix
555 Scherers Court, Columbus, OH, United States
Dallas
United States
Amazon Web Services, Equinix DA1, Equinix
1950 North Stemmons Freeway, Dallas, TX, United States
Amazon Web Services, Equinix DA3, Equinix
1950 North Stemmons Freeway, Dallas, TX, United States
Google Cloud, Equinix DA1, Equinix
1950 North Stemmons Freeway, Dallas, TX, United States
IBM Cloud, CyrusOne Lewisville (Dallas), CyrusOne
2501 S State Hwy 121, Lewisville, Dallas, TX, United States
IBM Cloud, Digital Realty DAL1, Digital Realty
2323 Bryan Street, Dallas, TX, United States
IBM Cloud, Digital Realty DAL3, Digital Realty
12301 North Stemmons Freeway, Dallas, TX, United States
IBM Cloud, Equinix DA1, Equinix
1950 North Stemmons Freeway, Dallas, TX, United States
IBM Cloud, QTS Dallas-Irving, QTS
6431 Longhorn Dr, Irving, Dallas, TX, United States
Microsoft Azure, CyrusOne Carrollton (Dallas), CyrusOne
1649 West Frankford Road, Carrollton, Dallas, TX, United States
Microsoft Azure, Digital Realty DAL1, Digital Realty
2323 Bryan Street, Dallas, TX, United States
Microsoft Azure, Equinix DA1, Equinix
1950 North Stemmons Freeway, Dallas, TX, United States
Oracle Cloud, Digital Realty DAL1, Digital Realty
2323 Bryan Street, Dallas, TX, United States
Oracle Cloud, Equinix DA3, Equinix
1950 North Stemmons Freeway, Dallas, TX, United States
Denver
United States
Amazon Web Services, CoreSite DE1, CoreSite
910 15th Street, Denver, CO, United States
Amazon Web Services, H5 Data Centers Denver, H5 Data Centers
5350 South Valentia Way, Denver, CO, United States
Google Cloud, CoreSite DE1, CoreSite
910 15th Street, Denver, CO, United States
Microsoft Azure, CoreSite DE1, CoreSite
910 15th Street, Denver, CO, United States
Houston
United States
Amazon Web Services, DataBank HOU1, DataBank
4001 Westpark Drive, Houston, TX, United States
Kansas City
United States
Amazon Web Services, 1102 Grand, 1102 Grand
1102 Grand Blvd, Kansas City, MO, United States
Las Vegas
United States
Amazon Web Services, Switch LAS Vegas 8 (The Core Campus), Switch
1 Superloop Circle, Las Vegas, NV, United States
Google Cloud, Switch LAS Vegas 8 (The Core Campus), Switch
1 Superloop Circle, Las Vegas, NV, United States
Microsoft Azure, Switch LAS Vegas 8 (The Core Campus), Switch
1 Superloop Circle, Las Vegas, NV, United States
Los Angeles
United States
Amazon Web Services, CoreSite LA1, CoreSite
1 Wilshire Boulevard, Los Angeles, CA, United States
Amazon Web Services, Equinix LA1, Equinix
1 Wilshire Boulevard, Los Angeles, CA, United States
Amazon Web Services, Equinix LA3, Equinix
600 West 7th Street, Los Angeles, CA, United States
Google Cloud, CoreSite LA1, CoreSite
1 Wilshire Boulevard, Los Angeles, CA, United States
Google Cloud, CoreSite LA2, CoreSite
900 North Alameda, Los Angeles, CA, United States
Google Cloud, Equinix LA1, Equinix
1 Wilshire Boulevard, Los Angeles, CA, United States
Microsoft Azure, CoreSite LA1, CoreSite
1 Wilshire Boulevard, Los Angeles, CA, United States
Microsoft Azure, Equinix LA1, Equinix
1 Wilshire Boulevard, Los Angeles, CA, United States
Miami
United States
Amazon Web Services, Digital Realty MIA1, Digital Realty
36 NE 2nd Street, Miami, FL, United States
Amazon Web Services, Equinix MI1, Equinix
50 NE 9th Street, Miami, FL, United States
Microsoft Azure, Equinix MI1, Equinix
50 NE 9th Street, Miami, FL, United States
Minneapolis
United States
Amazon Web Services, Cologix MIN1, Cologix
511 11th Avenue South, Minneapolis, MN, United States
New York
United States
Amazon Web Services, CoreSite NY1, CoreSite
32 Avenue of the Americas, New York, NY, United States
Amazon Web Services, Equinix NY1, Equinix
165 Halsey Street, Newark, New York, NY, United States
Google Cloud, Digital Realty NYC1, Digital Realty
111 8th Avenue, New York, NY, United States
Google Cloud, Equinix NY2, Equinix
275 Hartz Way, Secaucus, New York, NY, United States
Google Cloud, Equinix NY9, Equinix
111 8th Avenue, New York, NY, United States
Microsoft Azure, CoreSite NY1, CoreSite
32 Avenue of the Americas, New York, NY, United States
Microsoft Azure, Digital Realty NYC1, Digital Realty
111 8th Avenue, New York, NY, United States
Microsoft Azure, Equinix NY1, Equinix
165 Halsey Street, Newark, New York, NY, United States
Oracle Cloud, Digital Realty NYC1, Digital Realty
111 8th Avenue, New York, NY, United States
Phoenix
United States
Amazon Web Services, Cyxtera PHX1, Cyxtera
120 East Van Buren Street, Phoenix, AZ, United States
Amazon Web Services, Iron Mountain Phoenix, Iron Mountain
615 North 48th Street, Phoenix, AZ, United States
Microsoft Azure, EdgeConneX PHX01, EdgeConneX
3011 South 52nd Street, Tempe, Phoenix, AZ, United States
Oracle Cloud, Digital Realty PHX1, Digital Realty
120 East Van Buren Street, Phoenix, AZ, United States
Portland
United States
Amazon Web Services, Digital Realty PDX1, Digital Realty
3825 NW Aloclek Place, Hillsboro, Portland, OR, United States
Amazon Web Services, Flexential Portland - Hillsboro 2, Flexential
5737 NE Huffman St, Hillsboro, Portland, OR, United States
Salt Lake City
United States
Google Cloud, DataBank SLC1, DataBank
650 South Main Street, Salt Lake City, UT, United States
San Antonio
United States
Microsoft Azure, CyrusOne San Antonio I, CyrusOne
9999 Westover Hills Boulevard, San Antonio, TX, United States
Microsoft Azure, Frost Bank San Antonio, Frost Bank
San Antonio, TX, United States
Microsoft Azure, Microsoft San Antonio (SAT11), Microsoft
5150 Rogers Road, San Antonio, TX, United States
San Francisco
United States
Alibaba Cloud, Digital Realty SFO1, Digital Realty
200 Paul Avenue, San Francisco, CA, United States
Alibaba Cloud, Equinix SV5, Equinix
900 Trimble Road, San Jose, San Francisco, CA, United States
Amazon Web Services, CoreSite SV1, CoreSite
55 South Market Street, San Jose, San Francisco, CA, United States
Amazon Web Services, Digital Realty SFO1, Digital Realty
200 Paul Avenue, San Francisco, CA, United States
Amazon Web Services, Equinix SV1, Equinix
11 Great Oaks Boulevard, San Jose, San Francisco, CA, United States
Google Cloud, CoreSite SV1, CoreSite
55 South Market Street, San Jose, San Francisco, CA, United States
Google Cloud, Digital Realty SFO1, Digital Realty
200 Paul Avenue, San Francisco, CA, United States
Google Cloud, Equinix SV1, Equinix
11 Great Oaks Boulevard, San Jose, San Francisco, CA, United States
IBM Cloud, Digital Realty SFO1, Digital Realty
200 Paul Avenue, San Francisco, CA, United States
IBM Cloud, Equinix SV1, Equinix
11 Great Oaks Boulevard, San Jose, San Francisco, CA, United States
IBM Cloud, Equinix SV5, Equinix
900 Trimble Road, San Jose, San Francisco, CA, United States
Microsoft Azure, CoreSite SV2, CoreSite
1350 Duane Avenue, Santa Clara, San Francisco, CA, United States
Microsoft Azure, Equinix SV2, Equinix
1350 Duane Avenue, Santa Clara, San Francisco, CA, United States
Oracle Cloud, CoreSite SV1, CoreSite
55 South Market Street, San Jose, San Francisco, CA, United States
Oracle Cloud, Equinix SV1, Equinix
11 Great Oaks Boulevard, San Jose, San Francisco, CA, United States
Oracle Cloud, Equinix SV5, Equinix
900 Trimble Road, San Jose, San Francisco, CA, United States
Tencent Cloud, Equinix SV5, Equinix
900 Trimble Road, San Jose, San Francisco, CA, United States
Seattle
United States
Amazon Web Services, Equinix SE2, Equinix
2001 6th Avenue, Seattle, WA, United States
Amazon Web Services, Westin Building Exchange Seattle, Westin Building Exchange
2001 6th Avenue, Seattle, WA, United States
Google Cloud, Equinix SE2, Equinix
2001 6th Avenue, Seattle, WA, United States
Google Cloud, Equinix SE3, Equinix
2001 6th Avenue, Seattle, WA, United States
Microsoft Azure, Equinix SE2, Equinix
2001 6th Avenue, Seattle, WA, United States
Oracle Cloud, Equinix SE2, Equinix
2001 6th Avenue, Seattle, WA, United States
Washington
United States
Alibaba Cloud, Digital Realty IAD1, Digital Realty
21110 Stanwell Drive, Ashburn, Washington, DC, United States
Amazon Web Services, Digital Realty IAD1, Digital Realty
21110 Stanwell Drive, Ashburn, Washington, DC, United States
Amazon Web Services, Equinix DC2, Equinix
21715 Filigree Court, Ashburn, Washington, DC, United States
Amazon Web Services, Equinix DC6, Equinix
21715 Filigree Court, Ashburn, Washington, DC, United States
Google Cloud, Digital Realty IAD1, Digital Realty
21110 Stanwell Drive, Ashburn, Washington, DC, United States
Google Cloud, Equinix DC2, Equinix
21715 Filigree Court, Ashburn, Washington, DC, United States
IBM Cloud, Digital Realty IAD1, Digital Realty
21110 Stanwell Drive, Ashburn, Washington, DC, United States
IBM Cloud, Equinix DC11, Equinix
21715 Filigree Court, Ashburn, Washington, DC, United States
IBM Cloud, Equinix DC2, Equinix
21715 Filigree Court, Ashburn, Washington, DC, United States
Microsoft Azure, Digital Realty IAD1, Digital Realty
21110 Stanwell Drive, Ashburn, Washington, DC, United States
Microsoft Azure, Equinix DC2, Equinix
21715 Filigree Court, Ashburn, Washington, DC, United States
Oracle Cloud, Digital Realty IAD1, Digital Realty
21110 Stanwell Drive, Ashburn, Washington, DC, United States
Oracle Cloud, Equinix DC2, Equinix
21715 Filigree Court, Ashburn, Washington, DC, United States
Tencent Cloud, Equinix DC10, Equinix
21715 Filigree Court, Ashburn, Washington, DC, United States
Ho Chi Minh City
Vietnam
Alibaba Cloud, NTT GDC Ho Chi Minh HCMC1, NTT Global Data Centers
Saigon High-Tech Park, Ho Chi Minh City, Vietnam
"""

with open(file_path, "a", encoding="utf-8") as f:
    f.write(part5)

print(f"Part 5 wrote {len(part5)} characters.")
