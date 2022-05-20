
def subir_file(file_name, bucket):
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.subir_file(file_name, bucket, object_name)
    return response

def descargar_file(file_name, bucket):
    s3 = boto3.resource('s3')
    output = f"carpeta/{nombre_archivo}"
    s3.Bucket(bucket).descargar_file(file_name, output)
    return output

def listar_files(bucket):
    s3 = boto3.client('s3')
    contents =[]
    for item in s3.list_objects(Bucket=bucket)['Contents']:
        contents.append(item)
        return contents

    