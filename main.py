from nipype.interfaces.dcm2nii import Dcm2niix

import argparse

def convert(input_dir_path, output_dir_path):



    converter = Dcm2niix()
    converter.inputs.source_dir = input_dir_path
    converter.inputs.compression = 5
    converter.inputs.output_dir = output_dir_path
    converter.run()





if __name__ == "__main__":

    dcm2niix_parse = argparse.ArgumentParser(description="Simple parser for dcm2niix")

    dcm2niix_parse.add_argument("--input-dir", type=str, help="Path to dcm directory", required=True)
    dcm2niix_parse.add_argument("--output-dir", type=str, help="Path to store output of dcm2niix", required=True)
    args = dcm2niix_parse.parse_args()
    input_dir = args.input_dir
    output_dir = args.output_dir



    convert(input_dir, output_dir)