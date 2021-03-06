const FILE_URL = 'http://127.0.0.1:5000/api/file';
const DATA_URL = 'http://127.0.0.1:5000/api/data';

export async function uploadImageFile(form: HTMLFormElement): Promise<any> {
  const data = new FormData(form);
  const response = await fetch(FILE_URL, {
    method: "POST",
    mode: "cors",
    body: data
  });
  return await response.json();
}

export async function uploadImageData(data: string): Promise<any> {
  const response = await fetch(DATA_URL, {
    method: "POST",
    mode: "cors",
    body: data
  });
  return await response.json();
}
