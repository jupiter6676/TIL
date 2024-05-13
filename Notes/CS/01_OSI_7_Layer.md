<div style="border-radius: 3px; margin: 0.75rem 0 0; padding: 0.5rem; display: flex; position: relative; align-items: normal; word-break: break-word; background-color: #e9f7ff";>
    ℹ️ dasdfasdf
</div>

<div style="border-radius: 3px; margin: 0.75rem 0 0; padding: 0.5rem; display: flex; position: relative; align-items: normal; word-break: break-word; background-color: #e9ffef";>
    ✅ dasdfasdf
</div>

<div style="border-radius: 3px; margin: 0.75rem 0 0; padding: 0.5rem; display: flex; position: relative; align-items: normal; word-break: break-word; background-color: #fffee0";>
    ⚠️ dasdfasdf
</div>

<div style="border-radius: 3px; margin: 0.75rem 0 0; padding: 0.5rem; display: flex; position: relative; align-items: normal; word-break: break-word; background-color: #ffe9e9";>
    ⛔ dasdfasdf
</div>



# 1. OSI 7계층

## 1-1. OSI 7 계층

- 네트워크의 동작을 7 계층으로 나눠, 통신용 규약을 최대한 하나로 통합한 것
- 대부분 TCP/IP 프로토콜 스택 기반
- 네트워크 프로토콜을 모듈별로 개발할 수 있음



> 계층별 프로토콜 및 장비

| Layer |     Name     |                      Protocols                       |             장비             |
| :---: | :----------: | :--------------------------------------------------: | :--------------------------: |
|   7   | Application  |      HTTP, SMP, SMTP, STUN, TFTP, TELNET, POP3       |        ADC, NGFW, WAF        |
|   6   | Presentation |                    TLS, AFP, SSH                     |                              |
|   5   |   Session    |         L2TP, PPTP, NFS, RPC, RTCP, SIP, SSH         |                              |
|   4   |  Transport   |            TCP, UDP, SCTP, DCCP, AH, AEP             |   Load Balancer, Firewall    |
|   3   |   Network    |  ARP, IPv4, IPv6, NAT, APSec, VRRP, 라우팅 프로토콜  |      Router, L3 Switch       |
|   2   |  Data Link   | IEEE 802.2, RAPA, PPP, Frame Relay, ATM, Fiber Cable | Switch, Bridge, Network Card |
|   1   |   Physical   |          RS232, 100BaseTX, ISDN 등의 케이블          |       Cable, Hub, TAP        |

- 애플리케이션 계층 (상위 계층)

  - 7 ~ 5 계층
  - 애플리케이션 개발자는 상위 계층만을 고려
  - 데이터를 표현하는 데에 초점을 맞춤
  - Top-down

- 하위 계층

  - 1 ~ 4 계층

  - 네트워크 엔지니어는 하위 계층만을 고려

  - 데이터를 상대방에게 잘 전달하는 역할

  - Bottom-up

     

## 1-2. TCP/IP 프로토콜

- 이론보다 실용성에 중심을 둔 프로토콜
- 4 계층으로 구분



> OSI 7 계층과 TCP/IP 프로토콜

![image-20240205230859000](Assets/01_OSI_7_Layer.assets/image-20240205230859000.png)

- OSI 7 계층은 Data Flow 하위 계층과 Application 상위 계층으로 묶어서 구분
  - 이는 데이터 전달에 집중하는 영역과 애플리케이션에 집중하는 영역으로 구분한 것
- 애플리케이션 엔지니어와 네트워크 엔지니어가 고려할 부분에 대한 구분이 TCP/IP 프로토콜에서 더 명확하게 드러남



## 1-3. OSI 계층별 이해

### (1) 1 Layer - Physical

<div style="border-radius: 3px; margin: 0.75rem 0 0; padding: 0.5rem; display: flex; position: relative; align-items: normal; word-break: break-word; background-color: #e9f7ff";>
    <div style="height: 24px; width: 24px; box-sizing: content-box; padding-right: 8px; text-align: center; margin-top: 0.1rem;">
    	ℹ️
    </div>
    <div style="margin: 1px 0; flex: 1 0 0;">
        <p style="margin: 0;">물리적 연결과 관련된 정보를 정의하는 계층</p>
    </div>
</div>

- 주로 **전기 신호를 송수신**하는 데에 초점
  - 데이터를 전기 신호나 광 신호로 변환
  - 들어온 전기 신호를 잘 전달하는 것이 목적
  - 주소의 개념이 없어, 전기 신호가 들어온 포트를 제외한 모든 포트에 동일한 전기 신호를 전송
  - 전송 방법, 제어 신호, 기계적 속성 등을 정의



- 주요 장비

  - **허브** (Hub), **리피터** (Repeater)
    - 신호를 멀리 보내기 위한 증폭 장치
    - 허브는 리피터와 다르게 여러 장비를 연결할 수 있음
  - **케이블** (Cable)
    - 데이터를 전송하기 위한 물리적 장치
    - 이더넷, 광섬유 등
  - **트랜시버** (Tranceiver)
    - 컴퓨터의 랜 카드와 케이블을 연결하는 장비
    - 송신기와 수신기를 포함
      - 데이터를 전기 신호로 변환하여 케이블에 송출
      - 수신된 전기 신호를 데이터로 변환
  - **탭** (TAP)
    - 네트워크 모니터링 & 패킷 분석을 위해 전기 신호를 다른 장비로 복제하는 장비




### (2) 2 Layer - Data Link

<div style="border-radius: 3px; margin: 0.75rem 0 0; padding: 0.5rem; display: flex; position: relative; align-items: normal; word-break: break-word; background-color: #e9f7ff";>
    <div style="height: 24px; width: 24px; box-sizing: content-box; padding-right: 8px; text-align: center; margin-top: 0.1rem;">
    	ℹ️
    </div>
    <div style="margin: 1px 0; flex: 1 0 0;">
        <p style="margin: 0;">물리적 장비를 통해 전송되는 데이터의 오류를 검출 및 수정하여 신뢰성 있는 데이터 전송을 보장하는 계층</p>
    </div>
</div>

- **주소 정보**를 정의하고 **정확한 주소로 통신**하는 데에 초점
  - 출발지와 도착지의 주소를 확인하고, 정확히 보내졌는지 검사한 뒤 데이터를 처리
  - 전기 신호를 모아 데이터 형태로 처리
    - 프레임에 MAC 주소를 부여하고, 데이터에 대한 에러 탐지 및 수정을 담당
    - 이더넷 기반의 2 계층에서는 에러 탐지 역할만 수행
  - 수신자가 데이터를 받을 수 있는 상태인지 확인하는 작업 수행 (**Flow Control**)



> Flow Control

![image-20240206230859001](Assets/01_OSI_7_Layer.assets/image-20240206230859001.png)



- 대표적 프로토콜은 Ethernet, HDLC, PPP 등
- 네트워크 인터페이스 카드는 데이터를 **프레임**(Frame) 단위로 분리
- 프레임
  - 네트워크 통신에서 데이터를 전송하는 단위
  - 프레임은 Header, Data, Trailer의 요소로 구성되어 있음
    - Header: 출발지와 도착지의 MAC 주소가 포함되며, 프레임이 올바른 목적지로 전달되도록 함
    - Data: 실제 전송되는 데이터
    - Trailer: 오류 검출을 위한 CRC(Cyclic Redundancy Check)와 같은 오류 검출 코드를 포함하여, 데이터 전송 중 발생한 오류를 수신 측이 감지할 수 있음




> IEEE 802.3 Ethernet Frame

![image-20240208230859002](Assets/01_OSI_7_Layer.assets/image-20240208230859002.png)



- 주요 장비
  - **네트워크 인터페이스 카드 (NIC)**
    - PC나 서버에 네트워크를 연결해 주는 카드나 인터페이스
    - 랜 카드, 물리 네트워크 인터페이스, 이더넷 카드, 네트워크 어뎁터 등의 별칭이 존재
    - 동작 방식
      - 전기 신호를 데이터 형태로 변환
      - 목적지와 출발지의 MAC 주소 확인
      - 네트워크 인터페이스 카드의 MAC 주소 확인
      - 두 MAC 주소가 맞으면 데이터를 처리하고, 아니면 데이터를 폐기
  - **스위치**
    - 네트워크 중간에서 패킷을 받아, 필요한 곳에만 보내주는 중재자 역할
    - 단말의 MAC 주소와 단말의 포트 주소를 매핑한 MAC 주소 테이블을 가짐
  - **브리지**
    - 네트워크 세그먼트(큰 네트워크를 구성하는 작은 네트워크 집합)를 서로 연결하는 장치



- ✨ **MAC 주소**
  - 2 계층의 주소 체계로, MAC 주소를 통해 통신해야 할 포트를 지정하여 내보낼 수 있음
  - 네트워크 인터페이스 카드에는 고유 MAC 주소가 존재
    - MAC 주소를 이용해 전기 신호가 자신에게 오는 게 맞는지 확인
    - 맞을 경우 상위 계층에서 처리할 수 있도록 메모리에 적재
  - 스위치를 통해 단말의 MAC 주소와 연결 포트를 알 수 있음



### (3) 3 Layer - Network




---

- https://catsbi.notion.site/3560cc4231a64165a97334e8a714fa91
- https://www.guru99.com/layers-of-osi-model.html



- 2 계층
  - https://m.blog.naver.com/joo1020_kr/221471086900