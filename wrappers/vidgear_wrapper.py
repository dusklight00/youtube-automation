from vidgear.gears import WriteGear


def create_write_gear_instance(output_file):
    # output_params = {
    #     "-c:v": "libx264",
    #     "-crf": 22,
    #     "-map": 0,
    #     "-segment_time": 9,
    #     "-g": 9,
    #     "-sc_threshold": 0,
    #     "-force_key_frames": "expr:gte(t,n_forced*9)",
    #     "-clones": ["-f", "segment"],
    # }

    # Define writer with defined parameters
    writer = WriteGear(output=output_file, logging=True)
    return writer
