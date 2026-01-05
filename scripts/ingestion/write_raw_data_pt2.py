
file_path = "data/raw/cloud_infrastructure_map_raw.txt"

part2 = """
Local Zones
Metro Area
Zone Name, Parent Region, Access Facility
Buenos Aires
Argentina
Amazon Web Services, us-east-1-bue-1a, US East (Northern Virginia),
OVH, Buenos Aires, , Planned
Melbourne
Australia
Google Cloud, mel-zone1-1988, Melbourne (australia-southeast2),
Google Cloud, mel-zone1-4843, Melbourne (australia-southeast2),
Perth
Australia
Amazon Web Services, ap-southeast-2-per-1a, Asia Pacific (Sydney),
Microsoft Azure, Perth, , Planned
Sydney
Australia
Google Cloud, syd-zone1-1660, Sydney (australia-southeast1),
Google Cloud, syd-zone1-1605, Sydney (australia-southeast1),
Vienna
Austria
Amazon Web Services, eu-central-1-vie-1a, Europe (Frankfurt), Planned
OVH, Vienna, ,
Brussels
Belgium
Amazon Web Services, eu-west-3-bru-1a, Europe (Paris), Planned
OVH, Brussels, ,
Rio de Janeiro
Brazil
Amazon Web Services, us-east-1-rio-1a, US East (Northern Virginia), Planned
São Paulo
Brazil
Google Cloud, gru-zone1-1057, São Paulo (southamerica-east1),
Google Cloud, gru-zone1-165, São Paulo (southamerica-east1),
Google Cloud, gru-zone1-7580, São Paulo (southamerica-east1),
OVH, São Paulo, , Planned
Sofia
Bulgaria
OVH, Sofia, , Planned
London
Canada
Google Cloud, lhr-zone1-47, London (europe-west2),
Google Cloud, lhr-zone1-832, London (europe-west2),
Montréal
Canada
Google Cloud, yul-zone1-1944, Montreal (northamerica-northeast1),
Toronto
Canada
Amazon Web Services, ca-central-1-yto-1a, Canada (Central), Planned
Google Cloud, yyz-zone1-2206, Toronto (northamerica-northeast2),
Google Cloud, yyz-zone1-392, Toronto (northamerica-northeast2),
Vancouver
Canada
Amazon Web Services, ca-west-1-yvr-1a, Canada (West), Planned
Santiago
Chile
Amazon Web Services, us-east-1-scl-1a, US East (Northern Virginia),
Google Cloud, scl-zone1-1779, Santiago (southamerica-west1),
OVH, Santiago, , Planned
Hong Kong
China
Google Cloud, hkg-zone1-225, Hong Kong (asia-east2),
Google Cloud, hkg-zone1-1118, Hong Kong (asia-east2),
Bogotá
Colombia
Amazon Web Services, us-east-1-bog-1a, US East (Northern Virginia), Planned
Prague
Czech Republic
Amazon Web Services, eu-central-1-prg-1a, Europe (Frankfurt), Planned
OVH, Prague, ,
Abidjan
Côte d'Ivoire
OVH, Abidjan, , Planned
Copenhagen
Denmark
Amazon Web Services, eu-north-1-cph-1a, Europe (Stockholm),
OVH, Copenhagen, , Planned
Helsinki
Finland
Amazon Web Services, eu-north-1-hel-1a, US East (Northern Virginia),
Google Cloud, hem-zone1-7098, Finland (europe-north1),
Google Cloud, hem-zone1-8128, Finland (europe-north1),
OVH, Helsinki, , Planned
Marseille
France
OVH, Marseille, ,
Paris
France
Google Cloud, cdg-zone1-1536, Paris (europe-west9),
Google Cloud, cdg-zone1-181, Paris (europe-west9),
Google Cloud, cdg-zone1-3342, Paris (europe-west9),
Google Cloud, cdg-zone1-53, Paris (europe-west9),
Frankfurt
Germany
Google Cloud, fra-zone1-58, Frankfurt (europe-west3),
Google Cloud, fra-zone1-277, Frankfurt (europe-west3),
Google Cloud, fra-zone1-683, Frankfurt (europe-west3),
Hamburg
Germany
Amazon Web Services, eu-central-1-ham-1a, Europe (Frankfurt),
Athens
Greece
Amazon Web Services, eu-south-1-ath-1a, Europe (Milan), Planned
Bangalore
India
OVH, Bangalore, , Planned
Kolkata
India
Amazon Web Services, ap-south-1-ccu-1a, Asia Pacific (Mumbai),
Mumbai
India
Google Cloud, bom-zone1-2310, Mumbai (asia-south1),
Google Cloud, bom-zone1-554, Mumbai (asia-south1),
New Delhi
India
Amazon Web Services, ap-south-1-del-1a, Asia Pacific (Mumbai),
Google Cloud, del-zone1-1622, Delhi (asia-south2),
Google Cloud, del-zone1-2411, Delhi (asia-south2),
OVH, New Delhi, , Planned
Jakarta
Indonesia
Google Cloud, cgk-zone1-5865, Jakarta (asia-southeast2),
Google Cloud, cgk-zone1-8168, Jakarta (asia-southeast2),
Tel Aviv
Israel
Google Cloud, tlv-zone1-99030, Tel Aviv (me-west1),
Google Cloud, tlv-zone1-99047, Tel Aviv (me-west1),
Milan
Italy
Google Cloud, mil-zone1-1974, Milan (europe-west8),
Google Cloud, mil-zone1-3348, Milan (europe-west8),
Google Cloud, mil-zone1-99013, Milan (europe-west8),
Google Cloud, mil-zone1-99034, Milan (europe-west8),
OVH, Milan, ,
Osaka
Japan
Google Cloud, kix-zone1-1791, Osaka (asia-northeast2),
Google Cloud, kix-zone1-2072, Osaka (asia-northeast2),
Tokyo
Japan
Google Cloud, nrt-zone1-452, Tokyo (asia-northeast1),
Google Cloud, nrt-zone1-738, Tokyo (asia-northeast1), Planned
Google Cloud, nrt-zone1-1893, Tokyo (asia-northeast1),
Nairobi
Kenya
Amazon Web Services, af-south-1-nbo-1a, Africa (Cape Town), Planned
Luxembourg
Luxembourg
OVH, Luxembourg, , Planned
Mexico City
Mexico
OVH, Mexico City, , Planned
Santiago de Querétaro
Mexico
Amazon Web Services, us-east-1-qro-1a, US East (Northern Virginia),
Rabat
Morocco
OVH, Temara, ,
Amsterdam
Netherlands
Amazon Web Services, eu-central-1-ams-1a, Europe (Frankfurt), Planned
Google Cloud, ams-zone1-1236, Netherlands (europe-west4),
Google Cloud, ams-zone1-1320, Netherlands (europe-west4),
OVH, Amsterdam, ,
Auckland
New Zealand
Amazon Web Services, ap-southeast-2-akl-1a, Asia Pacific (Sydney),
OVH, Auckland, , Planned
Lagos
Nigeria
Amazon Web Services, af-south-1-los-1a, Africa (Cape Town),
Oslo
Norway
Amazon Web Services, eu-north-1-osl-1a, Europe (Stockholm), Planned
OVH, Oslo, , Planned
Muscat
Oman
Amazon Web Services, me-south-1-mct-1a, Middle East (Bahrain),
Lima
Peru
Amazon Web Services, us-east-1-lim-1a, US East (Northern Virginia),
Manila
Philippines
Amazon Web Services, ap-southeast-1-mnl-1a, Asia Pacific (Singapore),
Warsaw
Poland
Amazon Web Services, eu-central-1-waw-1a, Europe (Frankfurt),
Google Cloud, waw-zone1-2570, Warsaw (europe-central2),
Google Cloud, waw-zone1-509, Warsaw (europe-central2),
Lisbon
Portugal
Amazon Web Services, eu-south-2-lis-1a, Europe (Spain), Planned
OVH, Lisbon, , Planned
Bucharest
Romania
OVH, Bucharest, , Planned
Singapore
Singapore
Google Cloud, sin-zone1-388, Singapore (asia-southeast1),
Google Cloud, sin-zone1-2260, Singapore (asia-southeast1),
Johannesburg
South Africa
Amazon Web Services, af-south-1-jnb-1a, Africa (Cape Town), Planned
Google Cloud, jnb-zone1-850, Johannesburg (africa-south1),
Google Cloud, jnb-zone1-9338, Johannesburg (africa-south1),
Seoul
South Korea
Google Cloud, icn-zone1-3829, Seoul (asia-northeast3),
Google Cloud, icn-zone1-7573, Seoul (asia-northeast3),
Google Cloud, icn-zone1-7574, Seoul (asia-northeast3),
Google Cloud, icn-zone1-7674, Seoul (asia-northeast3),
Madrid
Spain
Google Cloud, mad-zone1-127, Madrid (europe-southwest1),
Google Cloud, mad-zone1-130, Madrid (europe-southwest1),
OVH, Madrid, ,
Stockholm
Sweden
OVH, Stockholm, , Planned
Zürich
Switzerland
Google Cloud, zrh-zone1-81, Zurich (europe-west6),
Google Cloud, zrh-zone1-1086, Zurich (europe-west6),
OVH, Zürich, ,
Taipei
Taiwan
Amazon Web Services, ap-northeast-1-tpe-1a, Asia Pacific (Tokyo),
Google Cloud, tsa-zone1-456, Taiwan (asia-east1),
Google Cloud, tsa-zone1-99004, Taiwan (asia-east1),
Google Cloud, tsa-zone1-2886, Taiwan (asia-east1),
Bangkok
Thailand
Amazon Web Services, ap-southeast-1-bkk-1a, Asia Pacific (Singapore),
Tunis
Tunisia
OVH, Tunis, , Planned
Dubai
United Arab Emirates
OVH, Dubai, , Planned
Manchester
United Kingdom
OVH, Manchester, , Planned
Atlanta
United States
Amazon Web Services, us-east-1-atl-2a, US East (Northern Virginia),
Google Cloud, dfw-zone1-4, Dallas (us-south1),
OVH, Atlanta, ,
Boston
United States
Amazon Web Services, us-east-1-bos-1a, US East (Northern Virginia),
OVH, Boston, , Planned
Chicago
United States
Amazon Web Services, us-east-1-chi-2a, US East (Northern Virginia),
OVH, Chicago, ,
Columbus
United States
Google Cloud, cmh-zone1-2377, Ohio,
Dallas
United States
Amazon Web Services, us-east-1-dfw-2a, US East (Northern Virginia),
OVH, Dallas, ,
Denver
United States
Amazon Web Services, us-west-2-den-1a, US West (Oregon),
OVH, Denver, ,
Fresno
United States
Amazon Web Services, us-west-2-pdx-1a, US West (Oregon),
Honolulu
United States
Amazon Web Services, us-west-2-hnl-1a, US West (Oregon),
Houston
United States
Amazon Web Services, us-east-1-iah-2a, US East (Northern Virginia),
Kansas City
United States
Amazon Web Services, us-east-1-mci-1a, US East (Northern Virginia),
Las Vegas
United States
Amazon Web Services, us-west-2-las-1a, US West (Oregon),
Google Cloud, las-zone1-770, Las Vegas (us-west4),
Los Angeles
United States
Amazon Web Services, us-west-2-lax-1a,us-west-2-lax-1b, US West (Oregon),
Google Cloud, lax-zone1-8, Los Angeles (us-west2),
Google Cloud, lax-zone1-19, Los Angeles (us-west2),
Google Cloud, lax-zone1-403, Los Angeles (us-west2),
Google Cloud, lax-zone1-333, Los Angeles (us-west2),
Microsoft Azure, Los Angeles, ,
OVH, Los Angeles, ,
Miami
United States
Amazon Web Services, us-east-1-mia-2a, US East (Northern Virginia),
OVH, Miami, ,
Minneapolis
United States
Amazon Web Services, us-east-1-msp-1a, US East (Northern Virginia),
New York
United States
Amazon Web Services, us-east-1-nyc-1a, US East (Northern Virginia),
OVH, Newark, ,
Omaha
United States
Google Cloud, cbf-zone1-575, Iowa (us-central1),
Philadelphia
United States
Amazon Web Services, us-east-1-phl-1a, US East (Northern Virginia),
Phoenix
United States
Amazon Web Services, us-west-2-phx-2a, US West (Oregon),
OVH, Phoenix, , Planned
Portland
United States
Google Cloud, pdx-zone1-1922, Oregon (us-west1),
Salt Lake City
United States
Google Cloud, slc-zone1-99001, Salt Lake City (us-west3),
OVH, Salt Lake City, , Planned
San Francisco
United States
OVH, Palo Alto, ,
Seattle
United States
Amazon Web Services, us-west-2-sea-1a, US West (Oregon),
OVH, Seattle, ,
St. Louis
United States
OVH, St. Louis, ,
Washington
United States
Google Cloud, iad-zone1-1, Northern Virginia (us-east4),
Google Cloud, iad-zone1-5467, Northern Virginia (us-east4),
Hanoi
Vietnam
Amazon Web Services, ap-southeast-1-han-1a, Asia Pacific (Singapore), Planned
"""

with open(file_path, "a", encoding="utf-8") as f:
    f.write(part2)

print(f"Part 2 wrote {len(part2)} characters.")
