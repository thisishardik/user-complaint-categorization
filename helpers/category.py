from helpers.yake import keyword_extraction_yake, sentence_tokenizer, generate_kw_info_from_kw_snt

def fetch_categories_map():

    categories = ["property", "family", "finiancial",
                "criminal", "business", "civil_litigation", "land_asset"]


    categories_map = {
        "property": "Property law is the area of law that governs the various forms of ownership in real property (land) and personal property. Property refers to legally protected claims to resources, such as land and personal property, including intellectual property.[1] Property can be exchanged through contract law, and if property is violated, one could sue under tort law to protect it.[1] The concept, idea or philosophy of property underlies all property law. In some jurisdictions, historically all property was owned by the monarch and it devolved through feudal land tenure or other feudal systems of loyalty and fealty.",
        "family": "Family law is the area of law that addresses family relationships. It includes creating family relationships and breaking them through divorce and termination of parental rights. This law addresses adoption, contested custody of children, etc. Family law is an area of the law that deals with family-related issues and domestic relations including, but not limited to the nature of marriage, the termination of marriage, and child-related issues.",
        "finiancial": "Financial law is the law and regulation of the insurance, derivatives, commercial banking, capital markets and investment management sectors.[1] Understanding Financial law is crucial to appreciating the creation and formation of banking and financial regulation, as well as the legal framework for finance generally. Financial law forms a substantial portion of commercial law, and notably a substantial proportion of the global economy, and legal billables are dependent on sound and clear legal policy pertaining to financial transactions.[2][3][4] Therefore financial law as the law for financial industries involves public and private law matters.[5] Understanding the legal implications of transactions and structures such as an indemnity, or overdraft is crucial to appreciating their effect in financial transactions.",
        "criminal": "the body of law that defines criminal offenses, regulates the apprehension, charging, and trial of suspected persons, and fixes penalties and modes of treatment applicable to convicted offenders. Criminal law is only one of the devices by which organized societies protect the security of individual interests and ensure the survival of the group. There are, in addition, the standards of conduct instilled by family, school, and religion; the rules of the office and factory; the regulations of civil life enforced by ordinary police powers; and the sanctions available through tort actions. The distinction between criminal law and tort law is difficult to draw with real precision, but in general one may say that a tort is a private injury whereas a crime is conceived as an offense against the public, although the actual victim may be an individual.",
        "business": "business law is the body of law which governs business and commerce and is often considered to be a branch of civil law and deals both with issues of private law and public law. Commercial law regulates corporate contracts, hiring practices, and the manufacture and sales of consumer goods. Many countries have adopted civil codes which contain comprehensive statements of their commercial law. ",
        "civil_litigation": "Civil litigation is the process in which civil matters are resolved in a court of law. Civil matters can be described as situations dealing with relationships between people, such as a marriage, or a contract dispute between corporations. Rather than a case being a person versus the government, as in a criminal matter, civil cases are an individual or business filing suit against another individual or business. ",
        "land_asset": "Land law is the form of law that deals with the rights to use, alienate, or exclude others from land. In many jurisdictions, these kinds of property are referred to as real estate or real property, as distinct from personal property.",
    }

    category_info = ""

    for key, value in categories_map.items():
        category_info = ""
        _, kw_lst = keyword_extraction_yake(value)
        kw_sent = sentence_tokenizer(kw_lst)
        category_info = generate_kw_info_from_kw_snt(kw_sent)
        categories_map[key] = category_info

    return categories_map