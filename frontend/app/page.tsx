"use client";
import { useState } from "react";

export default function Home() {
  const [text, setText] = useState("");
  const [clauses, setClauses] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [extracting, setExtracting] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleUpload = async (e: any) => {
    const file = e.target.files[0];
    if (!file) return;

    setLoading(true);
    setError("");
    setSuccess("");
    setClauses([]);
    
    const formData = new FormData();
    formData.append("file", file);
    
    try {
      const res = await fetch("http://localhost:8002/upload/", {
        method: "POST",
        body: formData,
      });
      
      if (!res.ok) {
        throw new Error(`Failed to upload file: ${res.status} ${res.statusText}`);
      }
      
      const data = await res.json();
      setText(data.content);
      setSuccess("File uploaded and processed successfully!");
    } catch (err: any) {
      console.error("Upload error:", err);
      setError(err.message || "An error occurred while uploading the file");
      setText("");
    } finally {
      setLoading(false);
    }
  };

  const handleExtractClauses = async () => {
    if (!text) {
      setError("Please upload a document first");
      return;
    }

    setExtracting(true);
    setError("");
    setSuccess("");
    setClauses([]);

    try {
      const res = await fetch("http://localhost:8002/extract/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
      });

      if (!res.ok) {
        const errorData = await res.json();
        throw new Error(`Failed to extract clauses: ${errorData.detail || res.statusText}`);
      }

      const data = await res.json();
      setClauses(data.extracted_data.clauses);
      setSuccess("Clauses extracted successfully!");
    } catch (err: any) {
      console.error("Extraction error:", err);
      setError(err.message || "An error occurred while extracting clauses");
    } finally {
      setExtracting(false);
    }
  };

  return (
    <div className="p-10 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-6 text-center">LawMind - Legal Document Analyzer</h1>
      
      <div className="bg-white rounded-lg shadow-md p-6 mb-6">
        <h2 className="text-xl font-semibold mb-4">Upload Document</h2>
        <input 
          type="file" 
          onChange={handleUpload} 
          className="block w-full text-sm text-gray-500
            file:mr-4 file:py-2 file:px-4
            file:rounded-md file:border-0
            file:text-sm file:font-semibold
            file:bg-blue-50 file:text-blue-700
            hover:file:bg-blue-100"
          accept=".pdf,.txt" 
        />
        
        {loading && (
          <div className="mt-4 flex items-center">
            <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-blue-500 mr-2"></div>
            <p>Uploading and processing document...</p>
          </div>
        )}
      </div>

      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded mb-6">
          <p><strong>Error:</strong> {error}</p>
        </div>
      )}

      {success && (
        <div className="bg-green-50 border border-green-200 text-green-700 px-4 py-3 rounded mb-6">
          <p><strong>Success:</strong> {success}</p>
        </div>
      )}

      {text && (
        <div className="bg-white rounded-lg shadow-md p-6 mb-6">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-xl font-semibold">Document Content</h2>
            <button 
              onClick={handleExtractClauses} 
              disabled={extracting}
              className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded disabled:opacity-50 flex items-center"
            >
              {extracting ? (
                <>
                  <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
                  Extracting Clauses...
                </>
              ) : "Extract Clauses"}
            </button>
          </div>
          
          <div className="border rounded p-4 max-h-96 overflow-y-auto">
            <pre className="whitespace-pre-wrap font-sans text-gray-700">
              {text}
            </pre>
          </div>
        </div>
      )}

      {clauses.length > 0 && (
        <div className="bg-white rounded-lg shadow-md p-6">
          <h2 className="text-2xl font-semibold mb-6 text-center">Extracted Clauses</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {clauses.map((clause, index) => (
              <div key={index} className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
                <div className="flex justify-between items-start mb-3">
                  <h3 className="font-bold text-lg text-gray-800">{clause.title}</h3>
                  <span className="inline-block bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded-full">
                    {clause.type}
                  </span>
                </div>
                <p className="text-gray-600">{clause.content}</p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}