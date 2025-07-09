import argparse

def preprocess_txt(root_path, file_format=".txt"):
    from langchain_community.document_loaders import DirectoryLoader, UnstructuredFileLoader
    # 加载文件夹中所有 .txt 和 .pdf 文件
    loader = DirectoryLoader(
        path=root_path,                         # 文档目录路径
        glob=f"./*{file_format}",                       # 可选：加载所有 .txt 文件，可写为 "**/*.*" 以包含所有类型
        loader_cls=UnstructuredFileLoader     # 使用非结构化文档加载器（兼容多种格式）
    )

    documents = loader.load()

    # 打印前几个文档的内容
    for doc in documents[:3]:
        print(doc.metadata)
        print(doc.page_content[:200], "\n")


def preprocess_pdf(path):
    from langchain_community.document_loaders import PyPDFLoader

    # 加载 PDF 文件（每一页为一个 Document）
    loader = PyPDFLoader(path)
    pages = loader.load()

    # 查看第一页的内容
    print(pages[0].metadata)
    print(pages[0].page_content[:300])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, default="docs/financial_term.txt")
    parser.add_argument("--file_type", type=str, default="txt", help=["txt", "pdf"])
    args = parser.parse_args()
    
    if args.file_type == "txt":
        preprocess_txt(args.path)
    
    elif args.file_type == "pdf":
        preprocess_pdf(args.path)
    
    else:
        print(f"file type not in [txt, pdf]")
    
    
    