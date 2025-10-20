from typing import TypedDict, Dict
from fastmcp import FastMCP, Context
from pydantic import BaseModel
# from fastmcp.resources import FileResource

class JobScribeRequestDict(BaseModel):
    id: str
    name: str
    company_name: str
    company_address: Dict[str, str]
    email: str

mcp = FastMCP("job-scribe")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

""" """
"""job: str, """
        # uri="resource://{name}/resume_pdf",
        # uri="resource://{job['company_name']}/{job['id']}",
""" @mcp.resource(
        uri="resource://resume_pdf",
        name="ResumePDF",
        mime_type="application/pdf",
        description="A Generated PDF"
)
def get_resume_pdf() -> bytes:
    with open("resume.pdf", "rb") as f:
        pdf_bytes = f.read()
    return pdf_bytes 
"""
"""Generates a PDF resume based on the provided resume data dictionary."""

def main():
    mcp.run()


if __name__ == "__main__":
    main()
