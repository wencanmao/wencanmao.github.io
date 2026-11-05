---
permalink: /
title: ""
excerpt: ""
description: "Wencan Mao, joint postdoctoral researcher at NII and The University of Tokyo. Edge computing, reinforcement learning, robotics, and intelligent transportation systems."
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Wencan Mao (**wencan_mao@nii.ac.jp**) is a joint postdoctoral researcher at the National Institute of Informatics (NII) and The University of Tokyo, Tokyo, Japan. She received her D.Sc. degree from the Department of Information and Communications Engineering, Aalto University, Espoo, Finland, in 2023; her M.S. degree in Mechanical Engineering from Aalto University in 2019; and her B.E. degree in Vehicle Engineering from Wuhan University of Technology, Wuhan, China, in 2017.

She has published in venues such as IEEE ICRA, IEEE Transactions on Mobile Computing, IEEE Transactions on Communications, IEEE Transactions on Wireless Communications, and IEEE Transactions on Vehicular Technology, and received the Best Paper Runner-up Award at IEEE INFOCOM 2026 Workshop. She also facilitates international collaborations between Asian and European universities.
Her research interests include edge computing, reinforcement learning, robotics, 6G, smart and sustainable cities, intelligent transportation systems, and the Internet of Things.

<div class="highlights">
  <div class="hl"><span class="hl-num" data-count="#journal-list">18</span><span class="hl-label">Journal papers</span></div>
  <div class="hl"><span class="hl-num" data-count="#conference-list">11</span><span class="hl-label">Conference papers</span></div>
  <a class="hl hl-cit" href="{{ site.author.googlescholar }}" hidden><span class="hl-num" id="hl-cit"></span><span class="hl-label">Citations</span></a>
  <div class="hl hl-award"><span class="hl-num">&#127942;</span><span class="hl-label">Best Paper Runner-up<br>IEEE INFOCOM 2026 Workshop</span></div>
</div>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[data-count]').forEach(function (el) {
      var list = document.querySelector(el.getAttribute('data-count'));
      if (list) { el.textContent = list.querySelectorAll(':scope > li').length; }
    });
    fetch('{{ url }}')
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (d) {
        if (d && d.message) {
          document.getElementById('hl-cit').textContent = d.message;
          document.querySelector('.hl-cit').hidden = false;
        }
      })
      .catch(function () {});
  });
</script>


# Education and Research
- *2026.04 – present* Joint postdoctoral researcher, Information Systems Architecture Science Research Division, National Institute of Informatics, Tokyo, Japan / Graduate School of Information Science and Technology, The University of Tokyo, Tokyo, Japan.
- *2024.07 – 2026.03* Postdoctoral researcher, Information Systems Architecture Science Research Division, National Institute of Informatics, Tokyo, Japan.
- *2023.12 – 2024.06* Postdoctoral researcher, Department of Computer Science, Aalto University, Espoo, Finland.
- *2023.09 – 2023.10* Visiting researcher, Department of Technology, Management and Economics, Technical University of Denmark, Copenhagen, Denmark.
- *2019.11 – 2023.11* Doctor of Science (D.Sc.), Department of Information and Communications Engineering, Aalto University, Espoo, Finland.
- *2018.09 – 2018.11* Exchange student, Department of Mechanical Engineering, Technical University of Munich, Munich, Germany.
- *2017.09 – 2019.06* Master of Science (M.S.), Department of Mechanical Engineering, Aalto University, Espoo, Finland.
- *2015.01 – 2015.07* Exchange student, School of Mechanical Engineering, University of Birmingham, Birmingham, UK.
- *2013.09 – 2017.06* Bachelor of Engineering (B.E.), School of Vehicle Engineering, Wuhan University of Technology, Wuhan, China.
{: .timeline}


# Publications
<sup>&#42;</sup> denotes equal contribution.
{: .note}

## Conferences
- <span class="venue">AINTEC'26</span> <span class="pub-title">MPDS-SAC: Multi-horizon Post-Decision State Soft Actor-Critic for Air-Ground Collaborative Sensing</span> Quanxi Zhou, **Wencan Mao**, Yunfei Chen, Junru Li, Jiachen Gong, Kensuke Fukuda, Manabu Tsukada, **21st Asian Internet Engineering Conference (AINTEC 2026)**, Taipei, Taiwan, 2026.
- <span class="venue">UbiComp'26</span> <span class="pub-title">NL2TL-Tree: Natural Language to Nested Temporal-Logic Trees for Robustness-Guided Flow-Matching Planning</span> Jiachen Gong, **Wencan Mao**, Ehsan Javanmardi, Yun Li, Quanxi Zhou, Manabu Tsukada, **Companion of the 2026 ACM International Joint Conference on Pervasive and Ubiquitous Computing and the 2026 ACM International Symposium on Wearable Computers (UbiComp/ISWC '26)**, Poster, 2026.
- <span class="venue">FINE'26</span> [Priority-Aware Hybrid Actor-Critic for Task Scheduling of UAV-Assisted Edge Computing](https://ieeexplore.ieee.org/abstract/document/11710909) Yunfei Chen, Quanxi Zhou, **Wencan Mao**, Guanzhi Lyu, Ye Tao, Kensuke Fukuda, Manabu Tsukada, **2026 IEEE International Conference on Future and Intelligent Networking (FINE)**, Osaka, Japan, Aug. 2026, pp. 246–253, doi: 10.1109/FINE71157.2026.00048.
- <span class="venue">ACCV'26</span> [CARE: Camera-Residual Reserves for First Sightings in Adaptive LiDAR Sensing](https://arxiv.org/abs/2608.24282) Jiachen Gong, Yun Li, Ehsan Javanmardi, **Wencan Mao**, Manabu Tsukada, **18th Asian Conference on Computer Vision (ACCV 2026)**, Osaka, Japan, 2026.
- <span class="venue">ICFEC'26</span> [UAV-Enabled Integrated Sensing, Semantic Communication, and Computation: Disaster-Oriented Edge Computing and Sensing](https://ieeexplore.ieee.org/abstract/document/11619137) Yaxi Liu, **Wencan Mao**, Xulong Li, Meng Gu, Yu Xiao, Wei Huangfu, Keping Long, **10th IEEE International Conference on Fog and Edge Computing (IEEE ICFEC 2026)**, Sydney, Australia, May 2026, pp. 65–72, doi: 10.1109/ICFEC69006.2026.00016.
- <span class="venue">INFOCOM'26</span> [A Dynamic Service-to-Slice Co-Evolutionary Framework Without Prior Labels in Society 5.0](https://ieeexplore.ieee.org/abstract/document/11571452) Zehui Li, **Wencan Mao**, Xulong Li, Yaxi Liu, Wei Huangfu, Yusheng Ji, **IEEE INFOCOM 2026 – IEEE Conference on Computer Communications Workshops (DOICT-IndSoc)**, Tokyo, Japan, May 2026, pp. 1–6, doi: 10.1109/INFOCOM59046.2026.11571452.
- <span class="venue">INFOCOM'26</span> [Deep Reinforcement Learning for Automated Guided Vehicle Trajectory Planning in Industry 4.0](https://ieeexplore.ieee.org/abstract/document/11571634) Quanxi Zhou<sup>&#42;</sup>, **Wencan Mao**<sup>&#42;</sup>, Yu Xiao, Manabu Tsukada, Yusheng Ji, **IEEE INFOCOM 2026 – IEEE Conference on Computer Communications Workshops (DOICT-IndSoc)**, Tokyo, Japan, May 2026, pp. 1–6, doi: 10.1109/INFOCOM59046.2026.11571634. <span class="award">&#127942; Best Paper Runner-up Award</span>
- <span class="venue">ICRA'26</span> [Trajectory Planning for UAV-Based Smart Farming Using Imitation-Based Triple Deep Q-Learning](https://ieeexplore.ieee.org/abstract/document/11696839) **Wencan Mao**<sup>&#42;</sup>, Quanxi Zhou<sup>&#42;</sup>, Tomás Couso Coddou, Manabu Tsukada, Yunling Liu, Yusheng Ji, **2026 IEEE International Conference on Robotics and Automation (ICRA)**, Vienna, Austria, Jun. 2026, pp. 20837–20844, doi: 10.1109/ICRA57385.2026.11696839.
- <span class="venue">MobiCom'24</span> [UAV-Assisted Integrated Sensing and Communication for Emergency Rescue Activities Based on Transfer Deep Reinforcement Learning](https://dl.acm.org/doi/10.1145/3636534.3698220) Yaxi Liu, **Wencan Mao**, Xulong Li, Wei Huangfu, Yusheng Ji, Yu Xiao, **Proceedings of the 30th Annual International Conference on Mobile Computing and Networking (ACM MobiCom '24), ISACom Workshop**, Washington, D.C., USA, Nov. 2024, pp. 2142–2147, doi: 10.1145/3636534.3698220.
- <span class="venue">hEART'24</span> [Understanding and predicting human behavior in interactions with autonomous systems in urban environments: a systematic review, challenges, and opportunities](https://transp-or.epfl.ch/heart/2024/abstracts/hEART_2024_paper_3882.pdf) Danya Li, **Wencan Mao**, Francisco Pereira, Yu Xiao, Xiang Su, Rico Krueger, **hEART 2024: 12th Symposium of the European Association for Research in Transportation**, Helsinki, Finland, 2024.
- <span class="venue">SMARTCOMP'22</span> [PhD Forum Abstract: Capacity Planning for Vehicular Fog Computing](https://ieeexplore.ieee.org/document/9821085) **Wencan Mao**, **2022 IEEE International Conference on Smart Computing (SMARTCOMP)**, Helsinki, Finland, Jun. 2022, pp. 186–187, doi: 10.1109/SMARTCOMP55677.2022.00047.
{: .pub-list #conference-list}

## Journals
- <span class="venue">TMC</span> [Trajectory Planning and Task Scheduling for UAVs in Dynamic Environments Using Feature-Driven Multi-Agent Reinforcement Learning](https://doi.org/10.1109/TMC.2026.3750340) Quanxi Zhou, **Wencan Mao**, Yilei Liang, Yixuan Liu, Manabu Tsukada, Jon Crowcroft, John C.S. Lui, Yusheng Ji, **IEEE Transactions on Mobile Computing**, early access, 2026, doi: 10.1109/TMC.2026.3750340.
- <span class="venue">TMC</span> [Service-Aware Joint Task Scheduling and Resource Allocation in Air-Ground Collaborative Multi-Tenant Network](https://ieeexplore.ieee.org/document/11774991) Boxin He, **Wencan Mao**, Kexin Yang, Yaxi Liu, Wei Huangfu, Fangxin Wang, Keping Long, **IEEE Transactions on Mobile Computing**, early access, 2026, doi: 10.1109/TMC.2026.3750465.
- <span class="venue">IEEE Network</span> [ComLLM: Toward A General Large Language Model for Semantic-Aware Network Optimization](https://ieeexplore.ieee.org/document/11641280) **Wencan Mao**, Quanxi Zhou, Yilei Liang, Yaxi Liu, Wei Huangfu, Manabu Tsukada, Jon Crowcroft, Yusheng Ji, **IEEE Network**, early access, 2026, doi: 10.1109/MNET.2026.3716787.
- <span class="venue">TMC</span> [Dynamic and Heterogeneous Network Slicing for Vehicular Edge Computing Based on Two-Timescale Reinforcement Learning](https://ieeexplore.ieee.org/abstract/document/11397758) Xulong Li, **Wencan Mao**, Xinyi Xu, Yaxi Liu, Wei Huangfu, Keping Long, Yu Xiao, Yusheng Ji, **IEEE Transactions on Mobile Computing**, vol. 25, no. 7, pp. 10939–10955, Jul. 2026, doi: 10.1109/TMC.2026.3665671.
- <span class="venue">TWC</span> [Bistatic-Enhancement MIMO ISAC: Joint Beamforming Design in Cell-Free Communication and Bistatic Radar Systems](https://ieeexplore.ieee.org/document/11215603) Boxin He, **Wencan Mao**, Yaxi Liu, Wei Huangfu, Fangxin Wang, Haijun Zhang, **IEEE Transactions on Wireless Communications**, vol. 25, pp. 5935–5951, 2026, doi: 10.1109/TWC.2025.3621759.
- <span class="venue">TCOM</span> [On-Demand Edge Computing Power Networks Assisted by Reconfigurable Intelligent Surface with Multi-Layer Scheme](https://ieeexplore.ieee.org/document/11152368) Boxin He, **Wencan Mao**, Yaxi Liu, Fangxin Wang, Wei Huangfu, **IEEE Transactions on Communications**, vol. 73, no. 12, pp. 15625–15638, Dec. 2025, doi: 10.1109/TCOMM.2025.3606656.
- <span class="venue">TVT</span> [Uncertainty-Aware Multi-Agent Reinforcement Learning for Anti-Interference Trajectory Planning of Cellular-Connected UAVs](https://ieeexplore.ieee.org/document/11150734) Quanxi Zhou, **Wencan Mao**, Jin Nakazato, Yusheng Ji, Manabu Tsukada, **IEEE Transactions on Vehicular Technology**, vol. 75, no. 2, pp. 2864–2880, Feb. 2026, doi: 10.1109/TVT.2025.3606201.
- <span class="venue">TCOM</span> [Energy-Efficient Joint Beamforming and Trajectory Optimization for UAV-Enabled Integrated Sensing and Communication](https://ieeexplore.ieee.org/document/11129138) Boxin He, **Wencan Mao**, Yaxi Liu, Wei Huangfu, Yu Xiao, Fangxin Wang, Yusheng Ji, **IEEE Transactions on Communications**, vol. 73, no. 12, pp. 13426–13440, Dec. 2025, doi: 10.1109/TCOMM.2025.3599902.
- <span class="venue">TVT</span> [Resource Allocation for UAV-Enabled Spatio-Temporal Crowdsourcing in Smart Cities](https://ieeexplore.ieee.org/document/11091546) Yaxi Liu, **Wencan Mao**, Xulong Li, Wei Huangfu, Yu Xiao, Yusheng Ji, Haijun Zhang, Keping Long, **IEEE Transactions on Vehicular Technology**, vol. 75, no. 1, pp. 1233–1249, Jan. 2026, doi: 10.1109/TVT.2025.3591850.
- <span class="venue">TCOM</span> [Joint Task Scheduling and Resource Allocation for UAV-Assisted Air-Ground Collaborative Integrated Sensing, Computation, and Communication](https://ieeexplore.ieee.org/document/11090168) Yaxi Liu, **Wencan Mao**, Xulong Li, Wei Huangfu, Yusheng Ji, Yu Xiao, Keping Long, **IEEE Transactions on Communications**, vol. 73, no. 11, pp. 10929–10945, Nov. 2025, doi: 10.1109/TCOMM.2025.3591748.
- <span class="venue">TCCN</span> [Multi-Modal Trajectory Planning for Emergency-Oriented Air-Ground Collaborative Sensing and Communication](https://ieeexplore.ieee.org/document/11063465) Yaxi Liu, Quanxi Zhou, **Wencan Mao**, Xulong Li, Wei Huangfu, Manabu Tsukada, Yusheng Ji, Keping Long, **IEEE Transactions on Cognitive Communications and Networking**, vol. 11, no. 5, pp. 3094–3111, Oct. 2025, doi: 10.1109/TCCN.2025.3585254.
- <span class="venue">TR Part F</span> [Analyzing the behaviors of pedestrians and cyclists in interactions with autonomous systems using controlled experiments: A literature review](https://www.sciencedirect.com/science/article/pii/S1369847825001950) Danya Li, **Wencan Mao**, Francisco C. Pereira, Yu Xiao, Xiang Su, Rico Krueger, **Transportation Research Part F: Traffic Psychology and Behaviour**, vol. 114, pp. 270–307, Oct. 2025, doi: 10.1016/j.trf.2025.05.031.
- <span class="venue">TCCN</span> [Self-Adjusting Network Slicing for Dynamic Heterogeneous Task Offloading in UAV-Enabled Mobile Edge Computing](https://ieeexplore.ieee.org/document/10981857) Xulong Li, **Wencan Mao**, Xinyi Xu, Yaxi Liu, Huifeng Zhang, Wei Huangfu, Keping Long, **IEEE Transactions on Cognitive Communications and Networking**, vol. 12, pp. 673–687, 2026, doi: 10.1109/TCCN.2025.3565942.
- <span class="venue">TCOM</span> [Radar Probing Optimization for Joint Beamforming and UAV Trajectory Design in UAV-Enabled Integrated Sensing and Communication](https://ieeexplore.ieee.org/document/10769423) Yaxi Liu, **Wencan Mao**, Boxin He, Wei Huangfu, Tianyao Huang, Haijun Zhang, Keping Long, **IEEE Transactions on Communications**, vol. 73, no. 6, pp. 4469–4485, Jun. 2025, doi: 10.1109/TCOMM.2024.3506917.
- <span class="venue">T-IV</span> [Multi-agent Reinforcement Learning-based Capacity Planning for On-demand Vehicular Fog Computing](https://ieeexplore.ieee.org/document/10584316) **Wencan Mao**, Jiaming Yin, Yushan Liu, Byungjin Cho, Yang Chen, Weixiong Rao, Yu Xiao, **IEEE Transactions on Intelligent Vehicles**, vol. 10, no. 2, pp. 1043–1057, Feb. 2025, doi: 10.1109/TIV.2024.3422375.
- <span class="venue">Syst. J.</span> [VFogSim: A Data-Driven Platform for Simulating Vehicular Fog Computing Environment](https://ieeexplore.ieee.org/document/10168727) Özgür Umut Akgül, **Wencan Mao**, Byungjin Cho, Yu Xiao, **IEEE Systems Journal**, vol. 17, no. 3, pp. 5002–5013, Sept. 2023, doi: 10.1109/JSYST.2023.3286329.
- <span class="venue">TVT</span> [On-Demand Vehicular Fog Computing for Beyond 5G Networks](https://ieeexplore.ieee.org/document/10164177) **Wencan Mao**, Özgür Umut Akgül, Byungjin Cho, Yu Xiao, Antti Ylä-Jääski, **IEEE Transactions on Vehicular Technology**, vol. 72, no. 12, pp. 15237–15253, Dec. 2023, doi: 10.1109/TVT.2023.3289862.
- <span class="venue">IoT-J</span> [Data-Driven Capacity Planning for Vehicular Fog Computing](https://ieeexplore.ieee.org/document/9684543) **Wencan Mao**, Özgür Umut Akgül, Abbas Mehrabi, Byungjin Cho, Yu Xiao, Antti Ylä-Jääski, **IEEE Internet of Things Journal**, vol. 9, no. 15, pp. 13179–13194, Aug. 2022, doi: 10.1109/JIOT.2022.3143872.
{: .pub-list #journal-list}

## Dissertations
- <span class="venue">D.Sc.</span> [Capacity Planning for Vehicular Fog Computing](https://aaltodoc.aalto.fi/items/64134a5d-8d64-4bce-b7f3-45c04df8623d) **Wencan Mao**, Doctoral dissertation, School of Electrical Engineering, Aalto University, Espoo, Finland, 2023, Aalto University publication series DOCTORAL THESES 172/2023, ISBN 978-952-64-1482-9.
- <span class="venue">M.S.</span> [Vision-based vehicle detection and tracking in intelligent transportation system](https://aaltodoc.aalto.fi/items/e76a35e4-58c8-44aa-8871-d114bddb0b45) **Wencan Mao**, Master's thesis, School of Engineering, Aalto University, Espoo, Finland, Jun. 2019.
{: .pub-list}


# Submitted Papers
## Conferences
- Q. Zhou<sup>&#42;</sup>, **W. Mao**<sup>&#42;</sup>, et al., [EIA-SEC: Improved Actor-Critic Framework for Multi-UAV Collaborative Control in Smart Agriculture](https://arxiv.org/abs/2512.18596), arXiv preprint.
- Q. Zhou<sup>&#42;</sup>, **W. Mao**<sup>&#42;</sup>, et al., [FM-EAC: Feature Model-Based Enhanced Actor-Critic for Multi-Task Control in Dynamic Environments](https://arxiv.org/abs/2512.15430), arXiv preprint.
{: .pub-list .compact}

## Journals
- Q. Xu, **W. Mao**, et al., Data-Driven Characterization and Insights of Network Metrics from a Systematic LLM-Agent Literature Mining, submitted to IEEE Transactions on Networking, 2026, <span class="status">under minor revision</span>.
- J. Wang, Q. Zhou, **W. Mao**, et al., Energy Harvesting UAV-Enabled Mobile Edge Computing with Sustainable Wireless Power Transfer Scheme, submitted to IEEE Transactions on Sustainable Computing, 2026, <span class="status">under major revision</span>.
- Q. Zhou, **W. Mao**, et al., EI-PANDA: Elite Imitation Point Aggregation Network with Dual Architecture for Trajectory Planning for UAV-Assisted Agricultural Systems, submitted to IEEE Transactions on Communications, 2026.
- Q. Zhou, **W. Mao**, et al., Decoupling Where-to-Fly from When-to-Upload: Quality- and AoI-Aware UAV-Enabled Spatio-Temporal Crowdsourcing, submitted to IEEE Transactions on Cognitive Communications and Networking, 2026.
- B. He, **W. Mao**, et al., Resource-Efficient Cell-Free MIMO ISAC: Joint Transmit Beamforming Design and Radar Receiving Base Station Selection, submitted to Science China Information Sciences, 2026.
<!--- M. Gu, **W. Mao**, et al., Beamforming and Reflection-Coefficient Matrix Design for RIS-Assisted Secure Integrated Sensing and Communication in Low-Altitude Activities, submitted to IEEE Transactions on Vehicular Technology, 2026. --->
- B. Cho, **W. Mao**, et al., Latency-Aware Pinching-Antenna Sensing of a Moving Target: Prediction and Its Geometric Limit, submitted to IEEE Transactions on Communications, 2026.
{: .pub-list .compact}


# Review Activities
## Conferences
- *2027* IEEE International Conference on Computer Communications and Networks (ICCCN 2027), TPC member.
- *2026–2027* IEEE International Conference on Communications (ICC 2026, ICC 2027), Wireless Communications Symposium, TPC member.
- *2026* IEEE Global Communications Conference (GLOBECOM 2026), TPC member.
- *2026* IEEE International Conference on Computer Communications (INFOCOM 2026) Workshops, TPC member.
- *2025–2026* ACM International Joint Conference on Pervasive and Ubiquitous Computing (UbiComp 2025/2026), poster/demo program committee.
- *2025* IEEE/CIC International Conference on Communications in China (ICCC 2025), TPC member.
- *2025* 18th IEEE/ACM International Conference on Utility and Cloud Computing / 12th IEEE/ACM International Conference on Big Data Computing, Applications and Technologies (UCC/BDCAT 2025), poster chair & TPC member.
- *2025* IEEE Global Communications Conference (GLOBECOM 2025), reviewer.
- *2025* IEEE Vehicular Technology Conference (VTC 2025-Spring & VTC 2025-Fall), reviewer.
{: .timeline}

## Journals
- *2026* IEEE Journal on Selected Areas in Communications (JSAC), reviewer.
- *2026* IEEE Transactions on Mobile Computing (TMC), reviewer.
- *2026* IEEE Transactions on Wireless Communications (TWC), reviewer.
- *2026* IEEE Transactions on Communications (TCOM), reviewer.
- *2026* IEEE Transactions on Vehicular Technology (TVT), reviewer.
- *2026* IEEE Network, reviewer.
- *2026* Scientific Reports, reviewer.
- *2025–2026* Pervasive and Mobile Computing, reviewer.
- *2024–2026* IEEE Transactions on Cognitive Communications and Networking (TCCN), reviewer.
- *2019–2023* IEEE Access, reviewer.
- *2019–2023* IEEE Internet of Things Journal (IoT-J), reviewer.
{: .timeline}


# Teaching Experiences
- *2026.08 – 2026.09* Lecturer, [Cooperative Interactive Vehicles (CIV) Summer School 2026](https://civ-summerschool.org/), Miyazaki, Japan.
- *2022.09 – 2023.12* Teaching assistant, Department of Information and Communications Engineering, Aalto University, Finland. Responsible for slide preparation, assignment design, and lecturing, and mentored 3 Master's students for the course "Smart Mobility: Systems, Services, and Applications".
- *2020.09 – 2023.09* Teaching assistant, Department of Computer Science, Aalto University, Finland. Responsible for slide preparation, personnel management, and activity organization for 100+ students, and tutored 7 Master's students for the course "Seminar in Computer Science: Internet, Data, and Things".
- *2019.09 – 2019.12* Pedagogical training, Department of Information and Communications Engineering, Aalto University, Finland.
{: .timeline}


# Research Funding and Grants
- *FY 2027* DAAD-JSPS Bilateral Joint Research Project, **Co-PI**, with the National Institute of Informatics (NII), Japan, The University of Tokyo, Japan, and the University of Göttingen, Germany. Submitted.
- *FY 2027* EIG CONCERT-Japan Joint Call on AI-Powered Robotics for Real-World Applications, **Co-PI**, with the National Institute of Informatics (NII), Japan, The University of Tokyo, Japan, Ruhr University Bochum (RUB), Germany, Industrial Research Institute for Automation and Measurements (PIAP), Poland, and Spanish National Research Council (CSIC), Spain. Submitted.
- *FY 2027* JSPS Grant-in-Aid for Scientific Research (B), **Co-PI**, with the National Institute of Informatics (NII), Japan, and The University of Tokyo, Japan. Submitted.
- *2023.05 – 2023.07* Aalto University Technology Support Foundation, **single applicant**. Awarded.
{: .timeline}


# Projects and Activities
- *2025.10 – present* Japan Society for the Promotion of Science (JSPS) Project, NII, Japan. Research on self-regulatory control and security assurance of large-scale decentralized systems.
- *2025.03 – present* Japan Science and Technology Agency (JST) CRONOS Project, Graduate School of Information Science and Technology, The University of Tokyo, Japan. Topics: LLM-Comm (vehicle-to-everything (V2X) communication with large language models (LLMs)), eHMI (human-machine interaction for autonomous vehicles), and autonomous driving field studies.
- *2024.07 – present* JST ASPIRE Project, Information Systems Architecture Science Research Division, National Institute of Informatics (NII), Japan & The University of Tokyo, Japan. Artificial intelligence (AI) for resource allocation, and resource allocation for AI.
- *2023.12 – 2024.06* Industrial Cooperation Project "Ensure", Department of Computer Science, Aalto University, Finland & Nokia Corporation, Finland. Developed a simulation and evaluation platform for energy-efficient 6G Tele-cloud.
- *2022.11 – 2023.12* Nordic Mobility Project, Industrial Internet of Things (IIoT) Hub, NTNU, Norway & KTH, Sweden & Lund University, Sweden & Aalto University, Finland & DTU, Denmark. Attended the IIoT Hub Conference 2022 at the Norwegian University of Science and Technology (NTNU), Norway, and the Student Meeting 2023 at Aalto University, including a Telia workshop and a visit to Maillefer Extrusion Oy.
- *2022.01 – 2023.11* Volunteer and facilitator, N4Women, Aalto University, Finland. Facilitated meetings for the group that supports women in STEM majors at Aalto University.
- *2019.06 – 2019.09* Research assistant, Department of Information and Communications Engineering, Aalto University, Finland. Established data-driven capacity planning and resource management platforms for fog computing.
- *2018.06 – 2018.08* Process and Tool Development Specialist Trainee, KONE Corporation, Shanghai, China. Managed large volumes of major-project installation data and people-flow data, communicated with field managers, project managers, and field engineers about the data, gathered feedback, and adjusted the installation progress.
- *2017.11 – 2018.05* International Team Project GLOBALDRIVE, Aalto University, Finland & Technical University of Munich (TUM), Germany. Team member of Geofusion (Aalto & TUM). Established a sensor fusion platform composed of LiDAR, GPS, and dual cameras to detect edge features and localize the vehicle in a high-precision map.
- *2015.12 – 2016.08* International Team Project "Connected Mobility Solution", Wuhan University of Technology, China. Team leader of Autopia (WUT). Envisioned a future transportation system composed of autonomous vehicles, cutting-edge vehicular technologies, and the Internet of Vehicles (IoV). Exhibited at the PACE 2016 Global Conference poster session, University of Cincinnati, USA.
{: .timeline}


# Honors and Awards
- *2026* Best Paper Runner-up Award, IEEE INFOCOM 2026 Workshop.
- *2023* Doctoral Graduate Scholarship, Aalto University.
- *2023* Grant, Foundation for Aalto University Science and Technology.
- *2022–2023* N4Women Volunteer, Department of Information and Communications Engineering, Aalto University.
- *2021–2023* Incentive Scholarship, Department of Computer Science, Aalto University.
- *2017–2019* Incentive Scholarship, Department of Mechanical Engineering, Aalto University.
- *2017–2019* Dean's List, Department of Mechanical Engineering, Aalto University.
- *2015* Exchange Program Scholarship, China Scholarship Council.
- *2013–2017* School-level Scholarship, Wuhan University of Technology.
- *2013–2017* Merit Student, Wuhan University of Technology.
{: .timeline}


# References
- [Prof. Kensuke Fukuda](http://www.flab.nii.ac.jp/), Professor, National Institute of Informatics, Japan (supervisor, 2026–present).
- [Prof. Manabu Tsukada](https://tlab.hongo.wide.ad.jp/), Associate Professor, The University of Tokyo, Japan (supervisor, 2026–present).
- [Prof. Yusheng Ji](https://klab-nii.github.io/jp/index.html), Professor Emeritus, National Institute of Informatics, Japan (supervisor, 2024–2026).
- [Prof. Antti Ylä-Jääski](https://users.aalto.fi/~anttiyj/), Professor Emeritus, Aalto University, Finland (supervisor, 2019–2024).
- [Prof. Yu Xiao](https://mobilecloud.aalto.fi/), Associate Professor, Aalto University, Finland (supervisor, 2019–2023).
- [Prof. John C.S. Lui](https://www.cse.cuhk.edu.hk/~cslui/), Professor, The Chinese University of Hong Kong (collaborator).
