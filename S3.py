import boto3

# Credenciales de acceso
aws_access_key_id = 'AKIAR55OBMAJSSHPJI2N'
aws_secret_access_key = 'TU_SECRET_KEY'
region_name = 'us-east-1'  # Puedes cambiar la región según tu necesidad

# Crear cliente para S3
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Listar los buckets disponibles
response = s3.list_buckets()

print("Buckets disponibles:")
for bucket in response['Buckets']:
    print(f"- {bucket['Name']}")
