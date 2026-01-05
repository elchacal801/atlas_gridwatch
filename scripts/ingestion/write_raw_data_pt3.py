
file_path = "data/raw/cloud_infrastructure_map_raw.txt"

part3 = """
On-Ramps
Metro Area
Cloud Service Provider, Data Center, Data Center Operator
Buenos Aires
Argentina
Amazon Web Services, Cirion BUE1, Cirion
Avenue del Campo 1301, Buenos Aires, Argentina
Google Cloud, Cirion BUE1, Lumen
Avenue del Campo 1301, Buenos Aires, Argentina
Oracle Cloud, Cirion BUE1, Lumen
Avenue del Campo 1301, Buenos Aires, Argentina
Brisbane
Australia
Amazon Web Services, NEXTDC B2, NEXTDC
454 St Pauls Terrace, Fortitude Valley, QLD, Australia
Google Cloud, NEXTDC B2, NEXTDC
454 St Pauls Terrace, Fortitude Valley, QLD, Australia
Canberra
Australia
Amazon Web Services, NEXTDC C1, NEXTDC
19 Battye St, Canberra, ACT, Australia
Google Cloud, Equinix CA1, Equinix
38 Vicars Street, Canberra, ACT, Australia
Microsoft Azure, CDC FY 1, Canberra Data Centres (CDC)
11 Tom Price Street, Fyshwick, ACT, Australia
Microsoft Azure, CDC HU1, Canberra Data Centres (CDC)
54 Sheppard St, Hume, ACT, Australia
Oracle Cloud, Equinix CA1, Equinix
38 Vicars Street, Canberra, ACT, Australia
Melbourne
Australia
Amazon Web Services, Equinix ME2, Equinix
578 Lorimer Street, Port Melbourne, VIC, Australia
Amazon Web Services, NEXTDC M1, NEXTDC
826 Lorimer St, Melbourne, VIC, Australia
Google Cloud, Equinix ME1, Equinix
578 Lorimer Street, Port Melbourne, VIC, Australia
Google Cloud, Equinix ME2, Equinix
578 Lorimer Street, Port Melbourne, VIC, Australia
Google Cloud, NEXTDC M2, NEXTDC
75 Sharps Rd, Melbourne, VIC, Australia
IBM Cloud, NEXTDC M1, NEXTDC
826 Lorimer St, Melbourne, VIC, Australia
Microsoft Azure, NEXTDC M1, NEXTDC
826 Lorimer St, Melbourne, VIC, Australia
Oracle Cloud, Equinix ME1, Equinix
578 Lorimer Street, Port Melbourne, VIC, Australia
Perth
Australia
Amazon Web Services, NEXTDC P1, NEXTDC
4 Millrose Dr, Perth, WA, Australia
Google Cloud, Equinix PE2, Equinix
37 Lemnos St, Perth, WA, Australia
IBM Cloud, Equinix PE2, Equinix
37 Lemnos St, Perth, WA, Australia
Microsoft Azure, NEXTDC P1, NEXTDC
4 Millrose Dr, Perth, WA, Australia
Sydney
Australia
Amazon Web Services, DigiCo SYD1 West, Global Switch
400 Harris Street, Ultimo, NSW, Australia
Amazon Web Services, Equinix SY3, Equinix
47 Bourke Road, Alexandria, NSW, Australia
Amazon Web Services, NEXTDC S2, NEXTDC
6-8 Giffnock Avenue, Sydney, NSW, Australia
Google Cloud, Equinix SY3, Equinix
47 Bourke Road, Alexandria, NSW, Australia
Google Cloud, NEXTDC S1, NEXTDC
4 Eden Park Drive, Sydney, NSW, Australia
IBM Cloud, DigiCo SYD1 West, Global Switch
400 Harris Street, Ultimo, NSW, Australia
IBM Cloud, Digital Realty SYD10, Digital Realty
1-23 Templar Road, Sydney, NSW, Australia
IBM Cloud, Equinix SY3, Equinix
47 Bourke Road, Alexandria, NSW, Australia
IBM Cloud, Equinix SY4, Equinix
200 Bourke Road, Alexandria, NSW, Australia
IBM Cloud, NEXTDC S1, NEXTDC
4 Eden Park Drive, Sydney, NSW, Australia
Microsoft Azure, Equinix SY2, Equinix
639 Gardeners Road, Mascot, NSW, Australia
Microsoft Azure, NEXTDC S1, NEXTDC
4 Eden Park Drive, Sydney, NSW, Australia
Oracle Cloud, Equinix SY4, Equinix
200 Bourke Road, Alexandria, NSW, Australia
Vienna
Austria
Amazon Web Services, Digital Realty VIE2, Digital Realty
Louis Haefliger Gasse 10, Vienna, Austria
Google Cloud, Digital Realty VIE2, Digital Realty
Louis Haefliger Gasse 10, Vienna, Austria
Microsoft Azure, Digital Realty VIE1, Digital Realty
Louis Haefliger Gasse 10, Vienna, Austria
Microsoft Azure, NTT GDC Vienna VIE1, NTT Global Data Centers
Computerstraße 4, Vienna, Austria
Manama
Bahrain
Amazon Web Services, AWS Middle East (Bahrain), Amazon Web Service
Manama, Bahrain
Brussels
Belgium
Google Cloud, Digital Realty BRU1, Digital Realty
Wezembeekstraat 2, Zaventem, Belgium
Campinas
Brazil
IBM Cloud, Ascenty VIN01, Digital Realty
Av João Batista Nunes 50, Vinhedo, Brazil
Microsoft Azure, Ascenty CPS01, Digital Realty
Av. Pierre Simon da Laplace, 1211, Campinas, Brazil
Oracle Cloud, Ascenty VIN01, Digital Realty
Av João Batista Nunes 50, Vinhedo, Brazil
Rio de Janeiro
Brazil
Amazon Web Services, Equinix RJ2, Equinix
Estrada Adhemar Bebiano 1380, Rio de Janeiro, Brazil
Google Cloud, CenturyLink Rio de Janeiro (Dom Pedro II, 329), CenturyLink
Av. Dom Pedro II, 329 - Sao Cristovao, Rio de Janeiro, Brazil
Google Cloud, Equinix RJ2, Equinix
Estrada Adhemar Bebiano 1380, Rio de Janeiro, Brazil
Microsoft Azure, Equinix RJ2, Equinix
Estrada Adhemar Bebiano 1380, Rio de Janeiro, Brazil
Santana de Parnaiba
Brazil
Huawei Cloud, ODATA SP01, Aligned Data Centers
Estrada dos Romeiros, 943, Santana de Parnaiba, Brazil
IBM Cloud, ODATA SP01, Aligned Data Centers
Estrada dos Romeiros, 943, Santana de Parnaiba, Brazil
São Paulo
Brazil
Amazon Web Services, Data Center Sao Paulo- SP1 (PIX TIVIT), Takoda
Rua Bento Branco de Andrade Filho, São Paulo, Brazil
Amazon Web Services, Equinix SP4, Equinix
Avenida Ceci, 1900 , Barueri, Brazil
Google Cloud, Ascenty SP02, Digital Realty
A. Roberto Pinto Sobrinho, 350, Osasco, Brazil
Google Cloud, Cirion São Paulo (Marginal 261), CenturyLink
Avenida Marginal, 261, São Paulo, Brazil
Google Cloud, Equinix SP4, Equinix
Avenida Ceci, 1900 , Barueri, Brazil
Huawei Cloud, Equinix SP1, Equinix
Rua Dr. Miguel Cuoto, 58, São Paulo, Brazil
Huawei Cloud, Huawei-Sao Paulo-VIVO, Telefonica
<Address not available>, São Paulo, Brazil
Huawei Cloud, Scala SGRUSP02, Scala Data Centers
Alameda Glete 700, São Paulo, Brazil
IBM Cloud, Ascenty JDI01, Digital Realty
Rua Presbítero Plinio Alves de Souza, 757, Jundiaí, Brazil
IBM Cloud, Equinix SP4, Equinix
Avenida Ceci, 1900 , Barueri, Brazil
Microsoft Azure, Data Center Sao Paulo- SP1 (PIX TIVIT), Takoda
Rua Bento Branco de Andrade Filho, São Paulo, Brazil
Microsoft Azure, Equinix SP2, Equinix
Alameda Araguaia 3641 - Alphaville, Barueri, Brazil
Oracle Cloud, Equinix SP4, Equinix
Avenida Ceci, 1900 , Barueri, Brazil
Tencent Cloud, ODATA SP03, Aligned Data Centers
Alameda Araguacema 187, Barueri, Brazil
Sofia
Bulgaria
Google Cloud, Equinix SO2, Equinix
33 Poruchik Nedelcho Bonchev Str, Sofia, Bulgaria
Google Cloud, Telepoint Sofia Centre, Telepoint
122 Ovche Pole Street, Sofia, Bulgaria
Calgary
Canada
Amazon Web Services, Equinix CL1, Equinix
315 8th Ave SW, Calgary, AB, Canada
Amazon Web Services, Equinix CL3, Equinix
5300 86th Avenue SE, Calgary, AB, Canada
Google Cloud, Equinix CL3, Equinix
5300 86th Avenue SE, Calgary, AB, Canada
Montréal
Canada
Amazon Web Services, Cologix MTL3, Cologix
1250 René Lévesque Ouest, Montréal, QC, Canada
Amazon Web Services, eStruxture MTL 1, eStruxture
800 Square Victoria, Montréal, QC, Canada
Google Cloud, Cologix MTL10, Cologix
530 Beriault Street, Longueuil, QC, Canada
Google Cloud, Cologix MTL3, Cologix
1250 René Lévesque Ouest, Montréal, QC, Canada
IBM Cloud, Colo-D1, **Colo-D**
2525 Canadien Street, Drummondville, QC, Canada
IBM Cloud, Colo-D2, **Colo-D**
Montréal, Canada
IBM Cloud, Cologix MTL2, Cologix
3000 Rene-Levesque, Verdun, QC, Canada
Microsoft Azure, Cologix MTL3, Cologix
1250 René Lévesque Ouest, Montréal, QC, Canada
Oracle Cloud, Cologix MTL3, Cologix
1250 René Lévesque Ouest, Montréal, QC, Canada
OVH, Cologix MTL1, Cologix
625 René Lévesque West, Montréal, QC, Canada
Quebec City
Canada
Microsoft Azure, Vantage Quebec City QC21, Vantage Data Centers
2675 Parc Technologique Blvd, Quebec City, QC, Canada
Toronto
Canada
Amazon Web Services, Equinix TR2, Equinix
45 Parliament, Toronto, ON, Canada
Amazon Web Services, TELEHOUSE Toronto 250 Front Street W, TELEHOUSE
250 Front Street W, Toronto, ON, Canada
Google Cloud, Equinix TR2, Equinix
45 Parliament, Toronto, ON, Canada
Google Cloud, TELEHOUSE Toronto 151 Front Street W, TELEHOUSE
151 Front Street, Toronto, ON, Canada
IBM Cloud, Cologix TOR1, Cologix
151 Front Street, Toronto, ON, Canada
IBM Cloud, Digital Realty YYZ10, Digital Realty
371 Gough Road, Markham, ON, Canada
IBM Cloud, Digital Realty YYZ11, Digital Realty
1 Century Place, Vaughan, ON, Canada
IBM Cloud, Equinix TR2, Equinix
45 Parliament, Toronto, ON, Canada
IBM Cloud, Serverfarm TOR1 Toronto, Serverfarm Realty
300 Bartor Road, Toronto, ON, Canada
Microsoft Azure, Cologix TOR1, Cologix
151 Front Street, Toronto, ON, Canada
Microsoft Azure, TELEHOUSE Toronto 905 King Street W, TELEHOUSE
905 King Street West, Toronto, ON, Canada
Oracle Cloud, Cologix TOR1, Cologix
151 Front Street, Toronto, ON, Canada
OVH, Equinix TR1, Equinix
151 Front Street, Toronto, ON, Canada
Vancouver
Canada
Amazon Web Services, Cologix VAN2, Cologix
1050 West Pender Street, Vancouver, BC, Canada
Amazon Web Services, Cologix VAN3, Cologix
2828 Natal Street, Vancouver, BC, Canada
Google Cloud, Cologix VAN2, Cologix
1050 West Pender Street, Vancouver, BC, Canada
Microsoft Azure, Cologix VAN1, Cologix
555 West Hastings Street, Vancouver, BC, Canada
Santiago
Chile
Amazon Web Services, SONDA Quilicura (Q1), SONDA
Victor Uribe 2211, Quilicura, Chile
Google Cloud, Ascenty CHL01, Digital Realty
Guacolda 2100, Renca, Chile
Google Cloud, Gtd Santiago (DC Panamericana), Grupo Gtd
Conchalí, Santiago, Chile
Google Cloud, Level 3 Santiago (Santa Marta de Huechuraba 6951), CenturyLink
Santa Marta de Huechuraba 6951, Huechuraba, Chile
Google Cloud, Location not available, Not specified
Santiago, Chile
Huawei Cloud, Claro Liray, Claro
Liray 1120, Santiago, Chile
Huawei Cloud, NextStream Panel 1, NextStream
Avenida Presidente Prieto # 266, Paine, Santiago, Chile
Microsoft Azure, EdgeConneX SCL01, EdgeConneX
Carretera General, Colina, Chile
Oracle Cloud, EdgeConneX SCL01, EdgeConneX
Carretera General, Colina, Chile
Valparaíso
Chile
Oracle Cloud, Scala SSCLCR01, Scala Data Centers
Av. Tupungato 3371, Curauma, Chile
Beijing
China
Alibaba Cloud, Beijing-Chaoyang-B, Alibaba Cloud
Beijing, China
Alibaba Cloud, Beijing-Chaoyang-C, Alibaba Cloud
Beijing, China
Alibaba Cloud, Beijing-Daxing-A , GDS Services
Beijing, China
Alibaba Cloud, Beijing-Daxing-E, China Unicom
Beijing, China
Alibaba Cloud, Beijing-Fengtai-A, Alibaba Cloud
Beijing, China
Alibaba Cloud, Beijing-Haidian-A, Alibaba Cloud
Beijing, China
Alibaba Cloud, Beijing-Langfang-A, Alibaba Cloud
Beijing, China
Alibaba Cloud, Beijing-Langfang-C, Alibaba Cloud
Beijing, China
Alibaba Cloud, Beijing-Shunyi-A, China Mobile
Beijing, China
Alibaba Cloud, Beijing-Shunyi-B, China Mobile
Beijing, China
Alibaba Cloud, China Telecom Beijing, China Telecom
Yongcheng N Rd, Haidian, Beijing, China
Alibaba Cloud, N-OR08 A, Not specified
Beijing, China
Amazon Web Services, CIDS Jiachuang IDC, CIDS China
21 Jiachuang 1st Road, Beijing, China
Amazon Web Services, SINNET Jiuxianqiao, SINNET
10 Jiuxianqiao North Road, Beijing, China
Huawei Cloud, Beijing-Langfang-A, Alibaba Cloud
Beijing, China
Huawei Cloud, China Telecom Beijing, China Telecom
Yongcheng N Rd, Haidian, Beijing, China
Huawei Cloud, China Telecom Langfang Runze, Chief Telecom
Beijing, China
Huawei Cloud, CNISP Data Nest 3, CNISP GROUP
Huo Ma Road, Tongzhou District, Beijing, China
Huawei Cloud, Jiuxianqiao Beijing Chaoyang, Jiuxianqiao
Beijing, China
Huawei Cloud, Langfang-GDS, GDS Services
Beijing, China
Huawei Cloud, N-OR08 A, Centrin Data Systems
Beijing, China
Microsoft Azure, China Telecom Beijing, China Telecom
Yongcheng N Rd, Haidian, Beijing, China
Microsoft Azure, GDS BJ1, GDS Services
11 E Ring Rd N, Beijing, China
Tencent Cloud, ap-beijing-2, Tencent Cloud
Beijing, China
Tencent Cloud, ap-beijing-3, Tencent Cloud
Beijing, China
Tencent Cloud, ap-beijing-5, Tencent Cloud
Beijing, China
Tencent Cloud, ap-beijing-6, Tencent Cloud
Beijing, China
Tencent Cloud, ap-beijing-7, Tencent Cloud
Beijing, China
Tencent Cloud, ap-beijing-bls-1, Tencent Cloud
Beijing, China
Tencent Cloud, ap-beijing-bls-2, Tencent Cloud
Beijing, China
Tencent Cloud, ap-beijing-bls-3, Tencent Cloud
Beijing, China
Tencent Cloud, ap-beijing-fsi-1, Tencent Cloud
Beijing, China
Tencent Cloud, ap-beijing-h-hldy, Tencent Cloud
Beijing, China
Tencent Cloud, ap-beijing-o-tg, Tencent Cloud
Beijing, China
Tencent Cloud, ap-financialcloud-beijing-c-kch, Tencent Cloud
Beijing, China
Tencent Cloud, ap-financialcloud-beijing-d-zhg, Tencent Cloud
Beijing, China
Tencent Cloud, ap-financialcloud-beijing-e-xh, Tencent Cloud
Beijing, China
Tencent Cloud, ap-financialcloud-beijing-f-sxq, Tencent Cloud
Beijing, China
Tencent Cloud, Beijing Boxing, Not specified
No.18, BoXing No.6 Road, Beijing, China
Tencent Cloud, GDS BJ2, GDS Services
KeChuang 3rd St, Beijing, China
Tencent Cloud, GDS BJ5, GDS Services
189 Changjin Rd, Beijing, China
Changsha
China
Alibaba Cloud, ap-cn-changsha-yl-A, China Unicom
Changsha, China
Tencent Cloud, ap-changsha-a-yg, Tencent Cloud
Changsha, China
Changshu
China
Alibaba Cloud, GDS CS1 P1, GDS Services
Changshu, China
Chengdu
China
Alibaba Cloud, Chengdu-Shuangliu-A, China Mobile
Chengdu, China
Alibaba Cloud, Chengdu-Shuangliu-B, China Unicom
Chengdu, China
Alibaba Cloud, GDS CD1, GDS Services
Tiansheng Road, High-tech Industry West Park, Chengdu, China
Huawei Cloud, Chengdu-Huawei, Huawei Cloud
Chengdu, China
Tencent Cloud, ap-chengdu-b-gh, Tencent Cloud
Chengdu, China
Tencent Cloud, GDS CD1, GDS Services
Tiansheng Road, High-tech Industry West Park, Chengdu, China
Chongqing
China
Tencent Cloud, GDS CQ1 P1, GDS Services
Chongqing, China
Tencent Cloud, Telstra PBS CQCS1, Telstra
No 8, Yunhan Dadao, Chongqing, China
Dalian
China
Alibaba Cloud, ap-cn-dalian-pld-A, China Mobile
Dalian, China
Fuzhou
China
Alibaba Cloud, China Telecom Fuzhou Dongmen, China Telecom
North Changle Rd, Fuzhou, China
Tencent Cloud, ap-fuzhou-a-ck, Tencent Cloud
Fuzhou, China
Guangzhou
China
Alibaba Cloud, Guangzhou-Development Zone-A, China Unicom
Guangzhou, China
Alibaba Cloud, Guangzhou-Huangpu-B, Alibaba Cloud
Guangzhou, China
Alibaba Cloud, Guangzhou-Huangpu-C, Alibaba Cloud
Guangzhou, China
Alibaba Cloud, GZIDC Guangzhou Qirui, GZIDC - New Generation International
Building C, Qirui Science and Technology Park, No. 1, , Guangzhou, China
Alibaba Cloud, Shenzhen-Longhua-A, China Telecom
Guangzhou, China
Alibaba Cloud, Shenzhen-Nanshan-A, China Mobile
Guangzhou, China
Huawei Cloud, China Telecom Guangzhou Yunpu, Chief Telecom
Guangzhou, China
Huawei Cloud, China Unicom Guangzhou Hualong, China Unicom
Guangzhou, China
Huawei Cloud, China Unicom Guangzhou Mingmei, China Unicom
Guangzhou, China
Huawei Cloud, Guangzhou-Huangpu-B, Alibaba Cloud
Guangzhou, China
Huawei Cloud, Huawei Dongguan Tuanbowa, Huawei Cloud
Guangzhou, China
Huawei Cloud, Huawei-Guangzhou-Daxuecheng, Huawei Cloud
Guangzhou, China
Huawei Cloud, Shenzhen-Baode, Carrier-neutral data center
Guangzhou, China
Huawei Cloud, Shenzhen-Futian, Not specified
Guangzhou, China
Huawei Cloud, Shenzhen-Nanshan, Not specified
Guangzhou, China
Huawei Cloud, Shenzhen-Yifeng, Yifeng
Guangzhou, China
Tencent Cloud, ap-guangzhou-3, Tencent Cloud
Guangzhou, China
Tencent Cloud, ap-guangzhou-4, Tencent Cloud
Guangzhou, China
Tencent Cloud, ap-guangzhou-5, Tencent Cloud
Guangzhou, China
Tencent Cloud, ap-guangzhou-a-kyl, Tencent Cloud
Guangzhou, China
Tencent Cloud, ap-guangzhou-c-dc, Tencent Cloud
Guangzhou, China
Tencent Cloud, ap-shenzhen-fsi-1, Tencent Cloud
Guangzhou, China
Tencent Cloud, GDS GZ1, GDS Services
31 Kefeng Rd, Guangzhou, China
Guiyang
China
Huawei Cloud, China Mobile Guiyang, China Mobile
Guiyang, China
Huawei Cloud, Huawei Guiyang Gui'an High-end Park, Huawei Cloud
Guiyang, China
Huawei Cloud, Huawei Guiyang Gui'an Qixinghu, Huawei Cloud
Guiyang, China
Hangzhou
China
Alibaba Cloud, Hangzhou-Deqing-A, China Unicom
Hangzhou, China
Alibaba Cloud, Hangzhou-Fuyang-A, China Telecom
Hangzhou, China
Alibaba Cloud, Hangzhou-Gongshu-A, China Unicom
Hangzhou, China
Alibaba Cloud, Hangzhou-Jianggan-B, VNET
Hangzhou, China
Alibaba Cloud, Hangzhou-Xiaoshan-A, China Unicom
Hangzhou, China
Alibaba Cloud, Hangzhou-Xiaoshan-B, China Telecom
Hangzhou, China
Alibaba Cloud, Hangzhou-Xiaoshan-D, China Mobile
Hangzhou, China
Alibaba Cloud, Hangzhou-Yuhang-B, Alibaba Cloud
Hangzhou, China
Alibaba Cloud, Hangzhou-Yuhang-C, Alibaba Cloud
Hangzhou, China
Tencent Cloud, ap-hangzhou-a-dg, Tencent Cloud
Hangzhou, China
Tencent Cloud, ap-hangzhou-b-xh, Tencent Cloud
Hangzhou, China
Tencent Cloud, ap-hangzhou-c-jg, Tencent Cloud
Hangzhou, China
Hefei
China
Tencent Cloud, ap-hefei-a-td, Tencent Cloud
Hefei, China
Heyuan
China
Alibaba Cloud, Heyuan-Gaoxin-A, Alibaba Cloud
Heyuan, China
Alibaba Cloud, Heyuan-Yuancheng-A, Alibaba Cloud
Heyuan, China
"""

with open(file_path, "a", encoding="utf-8") as f:
    f.write(part3)

print(f"Part 3 wrote {len(part3)} characters.")
