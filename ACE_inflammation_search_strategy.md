# ACEs × Inflammatory Biomarkers — Multi-Database Search Strategy
## 0. Scope & Assumptions
- Language: English (not applied by default; offered as optional filter).
- Humans only; provide optional filters to exclude animal-only papers.
- No year limits by default.
- Exposure: childhood adversity / ACEs / maltreatment / neglect / early life stress / family dysfunction / trauma before age 18.
- Outcomes: inflammatory biomarkers (broad inflammation terms + specific markers).
- **Version A (NARROW):** biomarker measured in child/adolescent samples (<18 at outcome measurement).
- **Version B (BROAD):** biomarker measured at any age, but exposure explicitly refers to childhood/early life.

## 1. Concept Map
### 1.1 Concept A — Childhood adversity / ACEs / maltreatment (FREE TEXT)
- Core terms: adverse childhood experience* OR ACE* OR childhood adversit* OR childhood trauma* OR child* trauma* OR early life stress OR early-life stress OR early life adversit* OR early-life adversit*.
- Maltreatment/abuse/neglect: child* maltreat* OR child* abuse* OR physical abuse OR sexual abuse OR emotional abuse OR psycholog* abuse OR child* neglect OR emotional neglect OR physical neglect OR supervisory neglect.
- Family dysfunction/household: family dysfunction* OR household dysfunction* OR domestic violence OR intimate partner violence OR parental substance use OR parental mental illness OR parental incarceration OR household incarceration OR parental divorce OR separation.
- Placement/instability: foster care OR out-of-home care OR institutionalization OR orphanage* OR placement instability.
- **Noise notes:** “ACE” is ambiguous (angiotensin-converting enzyme, adverse cardiac events, ACE inhibitors). Mitigation: pair ACE* with childhood/early-life terms or use phrase “adverse childhood experience*”.

### 1.2 Concept A — Controlled Vocabulary Candidates
- **MeSH (PubMed/MEDLINE):** Child Abuse; Child Neglect; Adverse Childhood Experiences; Early Life Stress; Stress, Psychological; Trauma and Stressor Related Disorders (use selectively); Domestic Violence; Family Relations; Foster Home Care; Institutionalization; Parent-Child Relations; Violence.
- **Emtree (Embase):** child abuse; child neglect; adverse childhood experience; early life stress; childhood trauma; domestic violence; family dysfunction; foster care; institutionalization; parent child relation; childhood adversity.
- **APA Thesaurus (PsycINFO):** Child Abuse; Child Neglect; Childhood Trauma; Early Life Stress; Adverse Childhood Experiences; Family Dysfunction; Domestic Violence; Foster Care; Institutionalization.
- *Candidate terms — verify mapping/explode in platform.*

### 1.3 Concept B — Inflammation / biomarkers (FREE TEXT)
- Broad inflammation terms: inflammation OR inflammatory OR acute phase OR acute-phase OR immune activation OR systemic inflammation OR low-grade inflammation.
- Cytokine/chemokine terms: cytokine* OR chemokine* OR interleukin* OR interferon* OR tumor necrosis factor.
- Specific biomarkers (>=10): CRP OR hsCRP OR hs-CRP OR “C-reactive protein” OR IL-6 OR interleukin-6 OR TNF-alpha OR tumor necrosis factor alpha OR IL-1beta OR interleukin-1 beta OR IL-8 OR interleukin-8 OR fibrinogen OR leukocyte* OR white blood cell* OR WBC OR ESR OR erythrocyte sedimentation rate OR suPAR OR GlycA OR NF-kB OR nuclear factor kappa B.
- Rationale: include both generic inflammation terms and specific biomarkers to capture studies that report biomarkers without using “inflammation” language and vice versa.

### 1.4 Concept B — Controlled Vocabulary Candidates
- **MeSH:** Inflammation; C-Reactive Protein; Cytokines; Chemokines; Interleukins; Tumor Necrosis Factor-alpha; Biomarkers; Acute-Phase Proteins; Leukocytes; Fibrinogen; Erythrocyte Sedimentation Rate.
- **Emtree:** inflammation; c reactive protein; cytokine; chemokine; interleukin; tumor necrosis factor; biomarker; acute phase protein; leukocyte; fibrinogen; erythrocyte sedimentation rate; immune activation.
- **APA Thesaurus (PsycINFO):** Inflammation; Cytokines; Interleukins; C Reactive Protein; Biomarkers; Immune System.
- *Candidate terms — verify mapping/explode in platform.*

### 1.5 Optional Concept C (ONLY if it materially improves recall)
- Psychoneuroimmunology (use as optional supplemental term if desired; may capture multidisciplinary studies that do not use standard biomarker phrasing).

## 2. Master Search Logic (Platform-Agnostic)
- **Version A (NARROW):** (Concept A) AND (Concept B) AND (child* OR adolescen* OR pediatric OR paediatric OR youth OR teen* OR minors)
- **Version B (BROAD):** (Concept A) AND (Concept B)
- Fielding guidance: use Title/Abstract and Keywords for free text; explode controlled vocabulary terms where available; pair “ACE*” with childhood/early-life terms to prevent ambiguity.

## 3. Database-Specific Queries (COPY/PASTE READY)
For each database, provide BOTH Version A and Version B.

### 3.1 PubMed
**Version A (NARROW)**
(
  (
    "Adverse Childhood Experiences"[Mesh] OR "Child Abuse"[Mesh] OR "Child Neglect"[Mesh] OR "Domestic Violence"[Mesh] OR "Foster Home Care"[Mesh] OR "Institutionalization"[Mesh] OR "Stress, Psychological"[Mesh]
    OR ("adverse childhood experience*"[tiab] OR "childhood adversit*"[tiab] OR "childhood trauma*"[tiab] OR "early life stress"[tiab] OR "early-life stress"[tiab] OR "child* maltreat*"[tiab] OR "child* abuse*"[tiab] OR "child* neglect"[tiab] OR "family dysfunction*"[tiab] OR "household dysfunction*"[tiab] OR "domestic violence"[tiab] OR "foster care"[tiab] OR "institutionalization"[tiab])
    OR (ACE*[tiab] AND (child* OR childhood OR "early life" OR early-life))
  )
  AND
  (
    "Inflammation"[Mesh] OR "C-Reactive Protein"[Mesh] OR "Cytokines"[Mesh] OR "Chemokines"[Mesh] OR "Interleukins"[Mesh] OR "Tumor Necrosis Factor-alpha"[Mesh] OR "Biomarkers"[Mesh] OR "Acute-Phase Proteins"[Mesh]
    OR (inflammation[tiab] OR inflammatory[tiab] OR "acute phase"[tiab] OR "acute-phase"[tiab] OR "immune activation"[tiab] OR cytokine*[tiab] OR chemokine*[tiab] OR interleukin*[tiab] OR interferon*[tiab] OR "tumor necrosis factor"[tiab] OR CRP[tiab] OR hsCRP[tiab] OR hs-CRP[tiab] OR "C-reactive protein"[tiab] OR IL-6[tiab] OR "interleukin-6"[tiab] OR TNF-alpha[tiab] OR "IL-1beta"[tiab] OR "interleukin-1 beta"[tiab] OR IL-8[tiab] OR "interleukin-8"[tiab] OR fibrinogen[tiab] OR leukocyte*[tiab] OR "white blood cell*"[tiab] OR WBC[tiab] OR ESR[tiab] OR "erythrocyte sedimentation rate"[tiab] OR suPAR[tiab] OR GlycA[tiab] OR "NF-kB"[tiab] OR "nuclear factor kappa B"[tiab])
  )
  AND (child*[tiab] OR adolescen*[tiab] OR pediatric[tiab] OR paediatric[tiab] OR youth[tiab] OR teen*[tiab] OR minors[tiab])
)

**Version B (BROAD)**
(
  (
    "Adverse Childhood Experiences"[Mesh] OR "Child Abuse"[Mesh] OR "Child Neglect"[Mesh] OR "Domestic Violence"[Mesh] OR "Foster Home Care"[Mesh] OR "Institutionalization"[Mesh] OR "Stress, Psychological"[Mesh]
    OR ("adverse childhood experience*"[tiab] OR "childhood adversit*"[tiab] OR "childhood trauma*"[tiab] OR "early life stress"[tiab] OR "early-life stress"[tiab] OR "child* maltreat*"[tiab] OR "child* abuse*"[tiab] OR "child* neglect"[tiab] OR "family dysfunction*"[tiab] OR "household dysfunction*"[tiab] OR "domestic violence"[tiab] OR "foster care"[tiab] OR "institutionalization"[tiab])
    OR (ACE*[tiab] AND (child* OR childhood OR "early life" OR early-life))
  )
  AND
  (
    "Inflammation"[Mesh] OR "C-Reactive Protein"[Mesh] OR "Cytokines"[Mesh] OR "Chemokines"[Mesh] OR "Interleukins"[Mesh] OR "Tumor Necrosis Factor-alpha"[Mesh] OR "Biomarkers"[Mesh] OR "Acute-Phase Proteins"[Mesh]
    OR (inflammation[tiab] OR inflammatory[tiab] OR "acute phase"[tiab] OR "acute-phase"[tiab] OR "immune activation"[tiab] OR cytokine*[tiab] OR chemokine*[tiab] OR interleukin*[tiab] OR interferon*[tiab] OR "tumor necrosis factor"[tiab] OR CRP[tiab] OR hsCRP[tiab] OR hs-CRP[tiab] OR "C-reactive protein"[tiab] OR IL-6[tiab] OR "interleukin-6"[tiab] OR TNF-alpha[tiab] OR "IL-1beta"[tiab] OR "interleukin-1 beta"[tiab] OR IL-8[tiab] OR "interleukin-8"[tiab] OR fibrinogen[tiab] OR leukocyte*[tiab] OR "white blood cell*"[tiab] OR WBC[tiab] OR ESR[tiab] OR "erythrocyte sedimentation rate"[tiab] OR suPAR[tiab] OR GlycA[tiab] OR "NF-kB"[tiab] OR "nuclear factor kappa B"[tiab])
  )
)

**Optional animals exclusion (not applied by default):**
NOT (animals[mh] NOT humans[mh])

### 3.2 Ovid MEDLINE
**Version A (NARROW)**
1. exp Adverse Childhood Experiences/ or exp Child Abuse/ or exp Child Neglect/ or exp Domestic Violence/ or exp Foster Home Care/ or exp Institutionalization/ or exp Stress, Psychological/
2. ("adverse childhood experience*" or "childhood adversit*" or "childhood trauma*" or "early life stress" or "early-life stress" or child* maltreat* or child* abuse* or child* neglect or family dysfunction* or household dysfunction* or domestic violence or foster care or institutionalization).ti,ab,kw.
3. (ACE* adj3 (child* or childhood or "early life" or early-life)).ti,ab,kw.
4. 1 or 2 or 3
5. exp Inflammation/ or exp C-Reactive Protein/ or exp Cytokines/ or exp Chemokines/ or exp Interleukins/ or exp Tumor Necrosis Factor-alpha/ or exp Biomarkers/ or exp Acute-Phase Proteins/ or exp Fibrinogen/ or exp Leukocytes/
6. (inflammation or inflammatory or "acute phase" or "acute-phase" or "immune activation" or cytokine* or chemokine* or interleukin* or interferon* or "tumor necrosis factor" or CRP or hsCRP or hs-CRP or "C-reactive protein" or IL-6 or "interleukin-6" or TNF-alpha or "IL-1beta" or "interleukin-1 beta" or IL-8 or "interleukin-8" or fibrinogen or leukocyte* or "white blood cell*" or WBC or ESR or "erythrocyte sedimentation rate" or suPAR or GlycA or "NF-kB" or "nuclear factor kappa B").ti,ab,kw.
7. 5 or 6
8. (child* or adolescen* or pediatric or paediatric or youth or teen* or minors).ti,ab,kw.
9. 4 and 7 and 8

**Version B (BROAD)**
1. exp Adverse Childhood Experiences/ or exp Child Abuse/ or exp Child Neglect/ or exp Domestic Violence/ or exp Foster Home Care/ or exp Institutionalization/ or exp Stress, Psychological/
2. ("adverse childhood experience*" or "childhood adversit*" or "childhood trauma*" or "early life stress" or "early-life stress" or child* maltreat* or child* abuse* or child* neglect or family dysfunction* or household dysfunction* or domestic violence or foster care or institutionalization).ti,ab,kw.
3. (ACE* adj3 (child* or childhood or "early life" or early-life)).ti,ab,kw.
4. 1 or 2 or 3
5. exp Inflammation/ or exp C-Reactive Protein/ or exp Cytokines/ or exp Chemokines/ or exp Interleukins/ or exp Tumor Necrosis Factor-alpha/ or exp Biomarkers/ or exp Acute-Phase Proteins/ or exp Fibrinogen/ or exp Leukocytes/
6. (inflammation or inflammatory or "acute phase" or "acute-phase" or "immune activation" or cytokine* or chemokine* or interleukin* or interferon* or "tumor necrosis factor" or CRP or hsCRP or hs-CRP or "C-reactive protein" or IL-6 or "interleukin-6" or TNF-alpha or "IL-1beta" or "interleukin-1 beta" or IL-8 or "interleukin-8" or fibrinogen or leukocyte* or "white blood cell*" or WBC or ESR or "erythrocyte sedimentation rate" or suPAR or GlycA or "NF-kB" or "nuclear factor kappa B").ti,ab,kw.
7. 5 or 6
8. 4 and 7

### 3.3 Ovid Embase
**Version A (NARROW)**
1. exp adverse childhood experience/ or exp child abuse/ or exp child neglect/ or exp domestic violence/ or exp foster care/ or exp institutionalization/ or exp psychological stress/
2. ("adverse childhood experience*" or "childhood adversit*" or "childhood trauma*" or "early life stress" or "early-life stress" or child* maltreat* or child* abuse* or child* neglect or family dysfunction* or household dysfunction* or domestic violence or foster care or institutionalization).ti,ab,kw.
3. (ACE* adj3 (child* or childhood or "early life" or early-life)).ti,ab,kw.
4. 1 or 2 or 3
5. exp inflammation/ or exp c reactive protein/ or exp cytokine/ or exp chemokine/ or exp interleukin/ or exp tumor necrosis factor/ or exp biomarker/ or exp acute phase protein/ or exp fibrinogen/ or exp leukocyte/
6. (inflammation or inflammatory or "acute phase" or "acute-phase" or "immune activation" or cytokine* or chemokine* or interleukin* or interferon* or "tumor necrosis factor" or CRP or hsCRP or hs-CRP or "C-reactive protein" or IL-6 or "interleukin-6" or TNF-alpha or "IL-1beta" or "interleukin-1 beta" or IL-8 or "interleukin-8" or fibrinogen or leukocyte* or "white blood cell*" or WBC or ESR or "erythrocyte sedimentation rate" or suPAR or GlycA or "NF-kB" or "nuclear factor kappa B").ti,ab,kw.
7. 5 or 6
8. (child* or adolescen* or pediatric or paediatric or youth or teen* or minors).ti,ab,kw.
9. 4 and 7 and 8

**Version B (BROAD)**
1. exp adverse childhood experience/ or exp child abuse/ or exp child neglect/ or exp domestic violence/ or exp foster care/ or exp institutionalization/ or exp psychological stress/
2. ("adverse childhood experience*" or "childhood adversit*" or "childhood trauma*" or "early life stress" or "early-life stress" or child* maltreat* or child* abuse* or child* neglect or family dysfunction* or household dysfunction* or domestic violence or foster care or institutionalization).ti,ab,kw.
3. (ACE* adj3 (child* or childhood or "early life" or early-life)).ti,ab,kw.
4. 1 or 2 or 3
5. exp inflammation/ or exp c reactive protein/ or exp cytokine/ or exp chemokine/ or exp interleukin/ or exp tumor necrosis factor/ or exp biomarker/ or exp acute phase protein/ or exp fibrinogen/ or exp leukocyte/
6. (inflammation or inflammatory or "acute phase" or "acute-phase" or "immune activation" or cytokine* or chemokine* or interleukin* or interferon* or "tumor necrosis factor" or CRP or hsCRP or hs-CRP or "C-reactive protein" or IL-6 or "interleukin-6" or TNF-alpha or "IL-1beta" or "interleukin-1 beta" or IL-8 or "interleukin-8" or fibrinogen or leukocyte* or "white blood cell*" or WBC or ESR or "erythrocyte sedimentation rate" or suPAR or GlycA or "NF-kB" or "nuclear factor kappa B").ti,ab,kw.
7. 5 or 6
8. 4 and 7

**Embase-specific note:** Emtree term names and explosion may differ from MEDLINE (verify preferred terms and mapping).

### 3.4 Web of Science Core Collection
**Version A (NARROW)**
TS=("adverse childhood experience*" OR "childhood adversit*" OR "childhood trauma*" OR "early life stress" OR "early-life stress" OR "child* maltreat*" OR "child* abuse*" OR "child* neglect" OR "family dysfunction*" OR "household dysfunction*" OR "domestic violence" OR "foster care" OR institutionalization OR (ACE* NEAR/3 (child* OR childhood OR "early life" OR early-life)))
AND TS=(inflammation OR inflammatory OR "acute phase" OR "acute-phase" OR "immune activation" OR cytokine* OR chemokine* OR interleukin* OR interferon* OR "tumor necrosis factor" OR CRP OR hsCRP OR hs-CRP OR "C-reactive protein" OR IL-6 OR "interleukin-6" OR TNF-alpha OR "IL-1beta" OR "interleukin-1 beta" OR IL-8 OR "interleukin-8" OR fibrinogen OR leukocyte* OR "white blood cell*" OR WBC OR ESR OR "erythrocyte sedimentation rate" OR suPAR OR GlycA OR "NF-kB" OR "nuclear factor kappa B")
AND TS=(child* OR adolescen* OR pediatric OR paediatric OR youth OR teen* OR minors)

**Version B (BROAD)**
TS=("adverse childhood experience*" OR "childhood adversit*" OR "childhood trauma*" OR "early life stress" OR "early-life stress" OR "child* maltreat*" OR "child* abuse*" OR "child* neglect" OR "family dysfunction*" OR "household dysfunction*" OR "domestic violence" OR "foster care" OR institutionalization OR (ACE* NEAR/3 (child* OR childhood OR "early life" OR early-life)))
AND TS=(inflammation OR inflammatory OR "acute phase" OR "acute-phase" OR "immune activation" OR cytokine* OR chemokine* OR interleukin* OR interferon* OR "tumor necrosis factor" OR CRP OR hsCRP OR hs-CRP OR "C-reactive protein" OR IL-6 OR "interleukin-6" OR TNF-alpha OR "IL-1beta" OR "interleukin-1 beta" OR IL-8 OR "interleukin-8" OR fibrinogen OR leukocyte* OR "white blood cell*" OR WBC OR ESR OR "erythrocyte sedimentation rate" OR suPAR OR GlycA OR "NF-kB" OR "nuclear factor kappa B")

### 3.5 Scopus
**Version A (NARROW)**
TITLE-ABS-KEY("adverse childhood experience*" OR "childhood adversit*" OR "childhood trauma*" OR "early life stress" OR "early-life stress" OR "child* maltreat*" OR "child* abuse*" OR "child* neglect" OR "family dysfunction*" OR "household dysfunction*" OR "domestic violence" OR "foster care" OR institutionalization OR (ACE* W/3 (child* OR childhood OR "early life" OR early-life)))
AND TITLE-ABS-KEY(inflammation OR inflammatory OR "acute phase" OR "acute-phase" OR "immune activation" OR cytokine* OR chemokine* OR interleukin* OR interferon* OR "tumor necrosis factor" OR CRP OR hsCRP OR hs-CRP OR "C-reactive protein" OR IL-6 OR "interleukin-6" OR TNF-alpha OR "IL-1beta" OR "interleukin-1 beta" OR IL-8 OR "interleukin-8" OR fibrinogen OR leukocyte* OR "white blood cell*" OR WBC OR ESR OR "erythrocyte sedimentation rate" OR suPAR OR GlycA OR "NF-kB" OR "nuclear factor kappa B")
AND TITLE-ABS-KEY(child* OR adolescen* OR pediatric OR paediatric OR youth OR teen* OR minors)

**Version B (BROAD)**
TITLE-ABS-KEY("adverse childhood experience*" OR "childhood adversit*" OR "childhood trauma*" OR "early life stress" OR "early-life stress" OR "child* maltreat*" OR "child* abuse*" OR "child* neglect" OR "family dysfunction*" OR "household dysfunction*" OR "domestic violence" OR "foster care" OR institutionalization OR (ACE* W/3 (child* OR childhood OR "early life" OR early-life)))
AND TITLE-ABS-KEY(inflammation OR inflammatory OR "acute phase" OR "acute-phase" OR "immune activation" OR cytokine* OR chemokine* OR interleukin* OR interferon* OR "tumor necrosis factor" OR CRP OR hsCRP OR hs-CRP OR "C-reactive protein" OR IL-6 OR "interleukin-6" OR TNF-alpha OR "IL-1beta" OR "interleukin-1 beta" OR IL-8 OR "interleukin-8" OR fibrinogen OR leukocyte* OR "white blood cell*" OR WBC OR ESR OR "erythrocyte sedimentation rate" OR suPAR OR GlycA OR "NF-kB" OR "nuclear factor kappa B")

### 3.6 PsycINFO
**(a) Ovid PsycINFO — Version A (NARROW)**
1. exp Adverse Childhood Experiences/ or exp Child Abuse/ or exp Child Neglect/ or exp Childhood Trauma/ or exp Early Life Stress/ or exp Domestic Violence/ or exp Foster Care/ or exp Institutionalization/
2. ("adverse childhood experience*" or "childhood adversit*" or "childhood trauma*" or "early life stress" or "early-life stress" or child* maltreat* or child* abuse* or child* neglect or family dysfunction* or household dysfunction* or domestic violence or foster care or institutionalization).ti,ab,kw.
3. (ACE* adj3 (child* or childhood or "early life" or early-life)).ti,ab,kw.
4. 1 or 2 or 3
5. exp Inflammation/ or exp Cytokines/ or exp Interleukins/ or exp C Reactive Protein/ or exp Biomarkers/ or exp Immune System/
6. (inflammation or inflammatory or "acute phase" or "acute-phase" or "immune activation" or cytokine* or chemokine* or interleukin* or interferon* or "tumor necrosis factor" or CRP or hsCRP or hs-CRP or "C-reactive protein" or IL-6 or "interleukin-6" or TNF-alpha or "IL-1beta" or "interleukin-1 beta" or IL-8 or "interleukin-8" or fibrinogen or leukocyte* or "white blood cell*" or WBC or ESR or "erythrocyte sedimentation rate" or suPAR or GlycA or "NF-kB" or "nuclear factor kappa B").ti,ab,kw.
7. 5 or 6
8. (child* or adolescen* or pediatric or paediatric or youth or teen* or minors).ti,ab,kw.
9. 4 and 7 and 8

**(a) Ovid PsycINFO — Version B (BROAD)**
1. exp Adverse Childhood Experiences/ or exp Child Abuse/ or exp Child Neglect/ or exp Childhood Trauma/ or exp Early Life Stress/ or exp Domestic Violence/ or exp Foster Care/ or exp Institutionalization/
2. ("adverse childhood experience*" or "childhood adversit*" or "childhood trauma*" or "early life stress" or "early-life stress" or child* maltreat* or child* abuse* or child* neglect or family dysfunction* or household dysfunction* or domestic violence or foster care or institutionalization).ti,ab,kw.
3. (ACE* adj3 (child* or childhood or "early life" or early-life)).ti,ab,kw.
4. 1 or 2 or 3
5. exp Inflammation/ or exp Cytokines/ or exp Interleukins/ or exp C Reactive Protein/ or exp Biomarkers/ or exp Immune System/
6. (inflammation or inflammatory or "acute phase" or "acute-phase" or "immune activation" or cytokine* or chemokine* or interleukin* or interferon* or "tumor necrosis factor" or CRP or hsCRP or hs-CRP or "C-reactive protein" or IL-6 or "interleukin-6" or TNF-alpha or "IL-1beta" or "interleukin-1 beta" or IL-8 or "interleukin-8" or fibrinogen or leukocyte* or "white blood cell*" or WBC or ESR or "erythrocyte sedimentation rate" or suPAR or GlycA or "NF-kB" or "nuclear factor kappa B").ti,ab,kw.
7. 5 or 6
8. 4 and 7

**(b) EBSCO PsycINFO — Version A (NARROW)**
(TI,AB,KW("adverse childhood experience*" OR "childhood adversit*" OR "childhood trauma*" OR "early life stress" OR "early-life stress" OR "child* maltreat*" OR "child* abuse*" OR "child* neglect" OR "family dysfunction*" OR "household dysfunction*" OR "domestic violence" OR "foster care" OR institutionalization OR (ACE* N3 (child* OR childhood OR "early life" OR early-life))))
AND (TI,AB,KW(inflammation OR inflammatory OR "acute phase" OR "acute-phase" OR "immune activation" OR cytokine* OR chemokine* OR interleukin* OR interferon* OR "tumor necrosis factor" OR CRP OR hsCRP OR hs-CRP OR "C-reactive protein" OR IL-6 OR "interleukin-6" OR TNF-alpha OR "IL-1beta" OR "interleukin-1 beta" OR IL-8 OR "interleukin-8" OR fibrinogen OR leukocyte* OR "white blood cell*" OR WBC OR ESR OR "erythrocyte sedimentation rate" OR suPAR OR GlycA OR "NF-kB" OR "nuclear factor kappa B"))
AND (TI,AB,KW(child* OR adolescen* OR pediatric OR paediatric OR youth OR teen* OR minors))

**(b) EBSCO PsycINFO — Version B (BROAD)**
(TI,AB,KW("adverse childhood experience*" OR "childhood adversit*" OR "childhood trauma*" OR "early life stress" OR "early-life stress" OR "child* maltreat*" OR "child* abuse*" OR "child* neglect" OR "family dysfunction*" OR "household dysfunction*" OR "domestic violence" OR "foster care" OR institutionalization OR (ACE* N3 (child* OR childhood OR "early life" OR early-life))))
AND (TI,AB,KW(inflammation OR inflammatory OR "acute phase" OR "acute-phase" OR "immune activation" OR cytokine* OR chemokine* OR interleukin* OR interferon* OR "tumor necrosis factor" OR CRP OR hsCRP OR hs-CRP OR "C-reactive protein" OR IL-6 OR "interleukin-6" OR TNF-alpha OR "IL-1beta" OR "interleukin-1 beta" OR IL-8 OR "interleukin-8" OR fibrinogen OR leukocyte* OR "white blood cell*" OR WBC OR ESR OR "erythrocyte sedimentation rate" OR suPAR OR GlycA OR "NF-kB" OR "nuclear factor kappa B"))

## 4. Optional Filters (NOT applied by default)
- **Humans only:** apply database-specific human limits or the PubMed animals exclusion line.
- **Animals exclusion (PubMed):** NOT (animals[mh] NOT humans[mh]).
- **Language=English:** apply only if required by protocol; risk of missing non-English studies with English abstracts.
- **Document type exclusions:** editorials/letters/news; use cautiously to avoid excluding brief reports.
- **Risk note:** over-filtering can reduce recall for early or interdisciplinary studies reporting biomarkers.

## 5. Iteration Log (MINIMUM 3 ROUNDS)
- **Round 1 → Round 2 (2025-02-14 10:00 UTC):** Expanded childhood adversity synonyms (family/household dysfunction, placement instability) and added more biomarker terms (suPAR, GlycA, NF-kB) to improve recall; added ACE ambiguity mitigation by coupling with childhood/early-life terms; broadened controlled vocabulary candidates. Likely impact: higher recall with moderate noise control.
- **Round 2 → Round 3 (2025-02-14 10:30 UTC):** Refined adjacency operators by platform (NEAR/x, W/x, adjN); added explicit pediatric population constraint for Version A; added optional filters section with cautions; normalized field tags and ensured copy/paste-ready formatting. Likely impact: improved precision in Version A and higher platform correctness without restricting Version B.

## 6. Validation & Coverage Check Plan
- **Golden set procedure:** identify 8–12 seed papers from preliminary scoping searches (e.g., key reviews or known cohort studies), then verify each is retrieved by Version A/B across at least two databases.
- **Synonym coverage audit:** verify inclusion of at least one term for each adversity domain (abuse, neglect, household dysfunction, early life stress) and each major biomarker group (CRP, cytokines, acute-phase proteins, immune activation).
- **Noise audit:** review top 50 results for common false positives (e.g., ACE inhibitor studies, adverse cardiac events); tighten ACE adjacency or add NOT terms if necessary without removing core child adversity concepts.
- **Deduplication guidance:** export with full records + abstracts; use DOI/PMID matching and title-year checks across databases.
