import os
import psycopg2

# UPLOAD Function - Handles single and multiple PDFs
def upload(pdf_input):
    def upload_single(pdf_path):
        pdf_name = os.path.basename(pdf_path).split(".pdf")[0]

        try:
            conn = psycopg2.connect(
                dbname="agent_db",
                user="postgres",
                password="pass",
                host="localhost",
                port="5432"
            )
            cursor = conn.cursor()

            insert_query = "INSERT INTO docs (name, pdf_data) VALUES (%s, %s)"
            cursor.execute(insert_query, (pdf_name, psycopg2.Binary(binary_data)))
            conn.commit()

            print(f"✅ Uploaded '{pdf_name}' successfully.")
            cursor.close()
            conn.close()

        except Exception as e:
            print(f"❌ Error uploading '{pdf_path}':", e)

    if isinstance(pdf_input, str):
        upload_single(pdf_input)
    elif isinstance(pdf_input, list):
        print("📦 Starting batch upload...")
        for path in pdf_input:
            upload_single(path)
        print("✅ Batch upload completed.")
    else:
        print("❌ Invalid input. Please provide a file path or list of file paths.")

# Example usage
if __name__ == "__main__":
    pdf_files = ["POSH.pdf"]  # Replace with your file paths
    upload(pdf_files)
