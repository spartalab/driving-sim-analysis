import pandas as pd


def main():
    no30lr = pd.read_csv("DAQ/PID10/NSF_CPS_NO30_LR_20210514170006.daq.csv")
    # no30lr/ no40lr/ yes30lr/ yes40lr:
    #         Lead Vehicle;     Driver
    # x axis: SCC_DynObj_Pos_0; VDS_Chassis_CG_Position_1
    # y axis: SCC_DynObj_Pos_1; VDS_Chassis_CG_Position_0

    # 1st int: straight
    # start: Lead Vehicle y axis value > -4374.36
    # end: Driver y axis value > -4205.00

    int1_start_t = no30lr[no30lr['SCC_DynObj_Pos_1'] > -4374.36]['timestamp'].iloc[1]
    print(int1_start_t)
    int1_end_t = no30lr[no30lr['VDS_Chassis_CG_Position_0'] > -4205.00]['timestamp'].iloc[1]
    print(int1_end_t)

    # 2nd int: left
    # start: Lead Vehicle y axis value > -1074.42
    # end: Driver x axis value < -2395.39
    int2_start_t = no30lr[no30lr['SCC_DynObj_Pos_1'] > -1074.42]['timestamp'].iloc[1]
    print(int2_start_t)
    int2_end_t = no30lr[no30lr['VDS_Chassis_CG_Position_1'] < -2395.39]['timestamp'].iloc[1]
    print(int2_end_t)

    # 3rd int: straight
    # start: Lead Vehicle x axis value < -5525.84
    # end: Driver x axis value < -5695.27
    int3_start_t = no30lr[no30lr['SCC_DynObj_Pos_0'] < -5525.84]['timestamp'].iloc[1]
    print(int3_start_t)
    int3_end_t = no30lr[no30lr['VDS_Chassis_CG_Position_1'] < -5695.27]['timestamp'].iloc[1]
    print(int3_end_t)

    # 4th int: right
    # start: Lead Vehicle x axis value < -8825.73
    # end: Driver y axis value > -904.95
    int4_start_t = no30lr[no30lr['SCC_DynObj_Pos_0'] < -8825.73]['timestamp'].iloc[1]
    print(int4_start_t)
    int4_end_t = no30lr[no30lr['VDS_Chassis_CG_Position_0'] > -904.95]['timestamp'].iloc[1]
    print(int4_end_t)

    # 5th int: straight
    # start: Lead Vehicle y axis value > 2225.55
    # end: Driver y axis value > 2395.23
    int5_start_t = no30lr[no30lr['SCC_DynObj_Pos_1'] > 2225.55]['timestamp'].iloc[1]
    print(int5_start_t)
    int5_end_t = no30lr[no30lr['VDS_Chassis_CG_Position_0'] > 2395.23]['timestamp'].iloc[1]
    print(int5_end_t)

    # For other drive types:
    # no30rl/ no40rl/ yes30rl/ yes40rl:
    #         Lead Vehicle;     Driver
    # x axis: SCC_DynObj_Pos_0; VDS_Chassis_CG_Position_1
    # y axis: SCC_DynObj_Pos_1; VDS_Chassis_CG_Position_0
    # 1st int: straight
    # start: Lead Vehicle y axis value > -4374.36
    # end: Driver y axis value > -4205.00
    # 2nd int: right
    # start: Lead Vehicle y axis value > -1074.42
    # end: Driver x axis value > -8825.60
    # 3rd int: straight
    # start: Lead Vehicle x axis value > -5695.27
    # end: Driver x axis value > -5525.84
    # 4th int: left
    # start: Lead Vehicle x axis value > -996.06
    # end: Driver y axis value > -904.95
    # 5th int: straight
    # start: Lead Vehicle y axis value > 2225.55
    # end: Driver y axis value > 2395.23



if __name__ == "__main__":
    main()
