from vidgear.gears import WriteGear


def create_writer_instance(output_file, fps=30):
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

    output_params = {"-input_framerate": fps}

    # Define writer with defined parameters
    writer = WriteGear(output=output_file, logging=True, **output_params)
    return writer
