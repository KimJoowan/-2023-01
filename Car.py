# 자동차 클래스 설계
class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.oil = 10  # 출고시 연료통에 채우는 연료량
        self.kmpl = 5  # 연비 리터당 달리는 거리
        self.odo = 0   # 출고 후 달린거리

    def __str__(self):
        return f"{self.name}({self.color})"

    def 상태(self):
        print(f"=========================")
        print(f"{self.name}:[{self.odo}]")
        print(f"oil:({self.oil})Liter")
        print(f"{self.oil * self.kmpl}km 운행가능합니다.")

    def 주유(self, 주유량):
        self.oil += 주유량
        print(f"=========================")
        print(f"({주유량})Liter를 주유하엿습니다.")
        self.상태()


    def 남은연료확인(self):
        # 남은연로로 주행가능한 거리를 계산한다
        주행가능거리 = self.oil * self.kmpl

        #주행가능한 거리가 70km 이하라면 종료메시지 풀력
        if 주행가능거리 <= 70:
            print(f"=========================")
            print("연료가 부족합니다.")
            print(f"{주행가능거리}km 운행가능합니다.")

    def 주행(self, 주행거리):
        # 현재 연료량 이 요청한 주행거리를 운행알수있는지 확인
        주행가능거리 = self.oil * self.kmpl

        # 주행이 불가능하면
        if 주행가능거리-주행거리 < 70:
            주행거리 = 주행가능거리
            print(f"연료부족으로 {주행거리}km만 운행합니다.")

        # 주행이 가능하면 다음단계로 진행
        else:
            연료소모량 = 주행거리 / self.kmpl
            self.odo += 주행거리
            self.oil -= 연료소모량

        # 소모된만큼 주행하면서 소모된 연료를 반영
            print(f"({주행거리})km을 운행하여습니다.")
            self.상태()
            self.남은연료확인()














