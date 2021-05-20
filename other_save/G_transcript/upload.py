# Imports the Google Cloud client library
#from google.cloud import storage

# Instantiates a client
#storage_client = storage.Client()

# # The name for the new bucket
# bucket_name = "supertest123"

# # Creates the new bucket
# bucket = storage_client.create_bucket(bucket_name)


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"
    from google.cloud import storage
    
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )
#upload_blob('clubhouse_audios','/home/ralfik555/Desktop/G_transcript/test_audio.wav','first_audio.wav')



def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)

