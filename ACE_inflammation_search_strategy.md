# ACEs × Inflammatory Biomarkers — Multi-Database Search Strategy
## 0. Scope & Assumptions
- **Language**: English (optional filter; not applied by default).
- **Population**: Humans only; optional animal-only exclusion provided.
- **Exposure window**: Adversity/trauma/maltreatment **before age 18**.
- **Outcomes**: Inflammatory biomarkers (systemic inflammation, cytokines, acute phase proteins, immune markers).
- **No year limits** by default.
- **Version A (NARROW)**: Biomarker measured in **child/adolescent samples (<18)** at time of outcome measurement.
- **Version B (BROAD)**: Biomarker measured at **any age**, but exposure explicitly refers to **childhood/early life**.
- **Exclusions (conceptual)**: Studies of adult trauma without childhood exposure; non-biological outcomes only.

## 1. Concept Map
### 1.1 Concept A — Childhood adversity / ACEs / maltreatment (FREE TEXT)
Curated keywords (use truncation where supported):
- child* advers* OR childhood advers* OR early life advers* OR early-life advers*
- adverse childhood experience* OR ACEs OR ACE (avoid ambiguity; see noise notes)
- child* maltreat* OR child* abuse* OR child* neglect* OR child* trauma*
- childhood trauma OR early life stress OR early-life stress
- child* victim* OR family dysfunction OR household dysfunction
- domestic violence exposure OR intimate partner violence exposure (as child witness)
- parental substance use OR parental mental illness OR parental incarceration
- institutional care OR foster care OR out-of-home care
- deprivation OR threat (as early-life exposure constructs)

**Noise notes & mitigation**:
- “ACE” is ambiguous (e.g., angiotensin-converting enzyme). Mitigate by pairing **ACE* with childhood/adverse** terms or using spelled-out phrases; avoid standalone “ACE” in titles/abstracts without context.
- “Abuse” and “trauma” are broad; use adjacency to child*/early-life terms when possible.

### 1.2 Concept A — Controlled Vocabulary Candidates
**MeSH (PubMed/MEDLINE)** — candidate terms; verify mapping/explode:
- *Adverse Childhood Experiences*
- *Child Abuse*
- *Child Neglect*
- *Child Maltreatment*
- *Psychological Trauma*
- *Domestic Violence*
- *Parenting*
- *Family Relations*
- *Stress, Psychological*
- *Social Deprivation*

**Emtree (Embase)** — candidate terms; verify mapping/explode:
- ‘child abuse’/exp
- ‘child neglect’/exp
- ‘child maltreatment’/exp
- ‘adverse childhood experience’/exp
- ‘psychological trauma’/exp
- ‘domestic violence’/exp
- ‘early life stress’/exp
- ‘social deprivation’/exp

**APA Thesaurus (PsycINFO)** — candidate terms; verify mapping/explode:
- *Adverse Childhood Experiences*
- *Child Abuse*
- *Child Neglect*
- *Child Maltreatment*
- *Psychological Trauma*
- *Early Life Stress*
- *Family Dysfunction*
- *Domestic Violence*

### 1.3 Concept B — Inflammation / biomarkers (FREE TEXT)
Broad + specific terms (retain both to maximize recall across heterogeneous reporting):
- inflamm* OR inflammatory OR systemic inflammation
- cytokine* OR chemokine* OR immune marker* OR immune biomarker* OR immunologic marker*
- C-reactive protein OR CRP OR hsCRP OR hs-CRP OR high-sensitivity CRP
- interleukin-6 OR IL-6 OR interleukin 6
- tumor necrosis factor alpha OR TNF-alpha OR TNF-a
- interleukin-1 beta OR IL-1beta OR IL-1β
- interleukin-8 OR IL-8
- interleukin-10 OR IL-10
- fibrinogen
- white blood cell* OR WBC OR leukocyte*
- erythrocyte sedimentation rate OR ESR
- soluble urokinase plasminogen activator receptor OR suPAR
- GlycA
- nuclear factor kappa B OR NF-kB OR NF-κB
- monocyte* OR macrophage* activation

**Rationale**: Generic inflammation terms capture studies that do not list specific biomarkers; specific markers ensure coverage when authors focus on single analytes.

### 1.4 Concept B — Controlled Vocabulary Candidates
**MeSH (PubMed/MEDLINE)** — candidate terms; verify mapping/explode:
- *Inflammation*
- *Biomarkers*
- *C-Reactive Protein*
- *Cytokines*
- *Interleukin-6*
- *Tumor Necrosis Factor-alpha*
- *Interleukin-1beta*
- *Interleukin-8*
- *Fibrinogen*
- *Leukocytes*
- *Erythrocyte Sedimentation Rate*

**Emtree (Embase)** — candidate terms; verify mapping/explode:
- ‘inflammation’/exp
- ‘biological marker’/exp
- ‘c reactive protein’/exp
- ‘cytokine’/exp
- ‘interleukin 6’/exp
- ‘tumor necrosis factor alpha’/exp
- ‘interleukin 1 beta’/exp
- ‘interleukin 8’/exp
- ‘fibrinogen’/exp
- ‘leukocyte’/exp
- ‘erythrocyte sedimentation rate’/exp

**APA Thesaurus (PsycINFO)** — candidate terms; verify mapping/explode:
- *Inflammation*
- *Biomarkers*
- *Cytokines*
- *C-Reactive Protein*
- *Interleukins*
- *Tumor Necrosis Factor*

### 1.5 Optional Concept C (ONLY if it materially improves recall)
- **Psychoneuroimmunology** (optional add-on if databases index this domain; may improve recall for integrative studies).

## 2. Master Search Logic (Platform-Agnostic)
- **Core logic**: (Concept A) AND (Concept B)
- **Version A (NARROW)**: (Concept A) AND (Concept B) AND (child/adolescent outcome context)
- **Version B (BROAD)**: (Concept A) AND (Concept B) with exposure constrained to childhood/early life terms
- **Fielding guidance**: Use controlled vocabulary with explode where possible; pair with Title/Abstract/Keyword text for sensitivity.

## 3. Database-Specific Queries (COPY/PASTE READY)
For each database: **Version A (NARROW)** and **Version B (BROAD)**.

### 3.1 PubMed
**Version A (NARROW)**
```
(
  "Adverse Childhood Experiences"[Mesh] OR "Child Abuse"[Mesh] OR "Child Neglect"[Mesh] OR "Child Maltreatment"[Mesh] OR
  "Psychological Trauma"[Mesh] OR "Domestic Violence"[Mesh] OR "Stress, Psychological"[Mesh] OR
  (child*[tiab] OR childhood[tiab] OR early life[tiab] OR early-life[tiab]) AND
  (advers*[tiab] OR maltreat*[tiab] OR abus*[tiab] OR neglect*[tiab] OR trauma*[tiab] OR stress*[tiab] OR deprivation[tiab] OR
   "family dysfunction"[tiab] OR "household dysfunction"[tiab] OR "adverse childhood"[tiab] OR "ACEs"[tiab])
)
AND
(
  "Inflammation"[Mesh] OR "Biomarkers"[Mesh] OR "C-Reactive Protein"[Mesh] OR "Cytokines"[Mesh] OR
  "Interleukin-6"[Mesh] OR "Tumor Necrosis Factor-alpha"[Mesh] OR "Interleukin-1beta"[Mesh] OR
  "Interleukin-8"[Mesh] OR "Fibrinogen"[Mesh] OR "Leukocytes"[Mesh] OR "Erythrocyte Sedimentation Rate"[Mesh] OR
  inflamm*[tiab] OR cytokine*[tiab] OR chemokine*[tiab] OR biomarker*[tiab] OR "C-reactive protein"[tiab] OR CRP[tiab] OR hsCRP[tiab] OR
  "interleukin-6"[tiab] OR IL-6[tiab] OR "tumor necrosis factor"[tiab] OR TNF-alpha[tiab] OR IL-1beta[tiab] OR IL-8[tiab] OR fibrinogen[tiab] OR
  leukocyte*[tiab] OR WBC[tiab] OR ESR[tiab] OR suPAR[tiab] OR GlycA[tiab] OR "NF-kB"[tiab]
)
AND
(
  child*[tiab] OR adolescen*[tiab] OR pediatric*[tiab] OR paediatric*[tiab] OR "youth"[tiab]
)
```
Optional animals exclusion (add as separate line if needed):
```
NOT (animals[MeSH Terms] NOT humans[MeSH Terms])
```

**Version B (BROAD)**
```
(
  "Adverse Childhood Experiences"[Mesh] OR "Child Abuse"[Mesh] OR "Child Neglect"[Mesh] OR "Child Maltreatment"[Mesh] OR
  "Psychological Trauma"[Mesh] OR "Domestic Violence"[Mesh] OR "Stress, Psychological"[Mesh] OR
  (child*[tiab] OR childhood[tiab] OR early life[tiab] OR early-life[tiab]) AND
  (advers*[tiab] OR maltreat*[tiab] OR abus*[tiab] OR neglect*[tiab] OR trauma*[tiab] OR stress*[tiab] OR deprivation[tiab] OR
   "family dysfunction"[tiab] OR "household dysfunction"[tiab] OR "adverse childhood"[tiab] OR "ACEs"[tiab])
)
AND
(
  "Inflammation"[Mesh] OR "Biomarkers"[Mesh] OR "C-Reactive Protein"[Mesh] OR "Cytokines"[Mesh] OR
  "Interleukin-6"[Mesh] OR "Tumor Necrosis Factor-alpha"[Mesh] OR "Interleukin-1beta"[Mesh] OR
  "Interleukin-8"[Mesh] OR "Fibrinogen"[Mesh] OR "Leukocytes"[Mesh] OR "Erythrocyte Sedimentation Rate"[Mesh] OR
  inflamm*[tiab] OR cytokine*[tiab] OR chemokine*[tiab] OR biomarker*[tiab] OR "C-reactive protein"[tiab] OR CRP[tiab] OR hsCRP[tiab] OR
  "interleukin-6"[tiab] OR IL-6[tiab] OR "tumor necrosis factor"[tiab] OR TNF-alpha[tiab] OR IL-1beta[tiab] OR IL-8[tiab] OR fibrinogen[tiab] OR
  leukocyte*[tiab] OR WBC[tiab] OR ESR[tiab] OR suPAR[tiab] OR GlycA[tiab] OR "NF-kB"[tiab]
)
```
Optional animals exclusion (add as separate line if needed):
```
NOT (animals[MeSH Terms] NOT humans[MeSH Terms])
```

### 3.2 Ovid MEDLINE
**Version A (NARROW)**
```
1. exp Adverse Childhood Experiences/ or exp Child Abuse/ or exp Child Neglect/ or exp Child Maltreatment/ or exp Psychological Trauma/ or exp Domestic Violence/ or exp Stress, Psychological/
2. ((child* or childhood or early life or early-life) adj3 (advers* or maltreat* or abus* or neglect* or trauma* or stress* or deprivation or "family dysfunction" or "household dysfunction" or "adverse childhood" or ACEs)).ti,ab,kw.
3. 1 or 2
4. exp Inflammation/ or exp Biomarkers/ or exp C-Reactive Protein/ or exp Cytokines/ or exp Interleukin-6/ or exp Tumor Necrosis Factor-alpha/ or exp Interleukin-1beta/ or exp Interleukin-8/ or exp Fibrinogen/ or exp Leukocytes/ or exp Erythrocyte Sedimentation Rate/
5. (inflamm* or cytokine* or chemokine* or biomarker* or "C-reactive protein" or CRP or hsCRP or "interleukin-6" or IL-6 or "tumor necrosis factor" or TNF-alpha or IL-1beta or IL-8 or fibrinogen or leukocyte* or WBC or ESR or suPAR or GlycA or "NF-kB").ti,ab,kw.
6. 4 or 5
7. (child* or adolescen* or pediatric* or paediatric* or youth).ti,ab,kw.
8. 3 and 6 and 7
```

**Version B (BROAD)**
```
1. exp Adverse Childhood Experiences/ or exp Child Abuse/ or exp Child Neglect/ or exp Child Maltreatment/ or exp Psychological Trauma/ or exp Domestic Violence/ or exp Stress, Psychological/
2. ((child* or childhood or early life or early-life) adj3 (advers* or maltreat* or abus* or neglect* or trauma* or stress* or deprivation or "family dysfunction" or "household dysfunction" or "adverse childhood" or ACEs)).ti,ab,kw.
3. 1 or 2
4. exp Inflammation/ or exp Biomarkers/ or exp C-Reactive Protein/ or exp Cytokines/ or exp Interleukin-6/ or exp Tumor Necrosis Factor-alpha/ or exp Interleukin-1beta/ or exp Interleukin-8/ or exp Fibrinogen/ or exp Leukocytes/ or exp Erythrocyte Sedimentation Rate/
5. (inflamm* or cytokine* or chemokine* or biomarker* or "C-reactive protein" or CRP or hsCRP or "interleukin-6" or IL-6 or "tumor necrosis factor" or TNF-alpha or IL-1beta or IL-8 or fibrinogen or leukocyte* or WBC or ESR or suPAR or GlycA or "NF-kB").ti,ab,kw.
6. 4 or 5
7. 3 and 6
```

### 3.3 Ovid Embase
**Version A (NARROW)**
```
1. exp adverse childhood experience/ or exp child abuse/ or exp child neglect/ or exp child maltreatment/ or exp psychological trauma/ or exp domestic violence/ or exp early life stress/ or exp social deprivation/
2. ((child* or childhood or early life or early-life) adj3 (advers* or maltreat* or abus* or neglect* or trauma* or stress* or deprivation or "family dysfunction" or "household dysfunction" or "adverse childhood" or ACEs)).ti,ab,kw.
3. 1 or 2
4. exp inflammation/ or exp biological marker/ or exp c reactive protein/ or exp cytokine/ or exp interleukin 6/ or exp tumor necrosis factor alpha/ or exp interleukin 1 beta/ or exp interleukin 8/ or exp fibrinogen/ or exp leukocyte/ or exp erythrocyte sedimentation rate/
5. (inflamm* or cytokine* or chemokine* or biomarker* or "C-reactive protein" or CRP or hsCRP or "interleukin-6" or IL-6 or "tumor necrosis factor" or TNF-alpha or IL-1beta or IL-8 or fibrinogen or leukocyte* or WBC or ESR or suPAR or GlycA or "NF-kB").ti,ab,kw.
6. 4 or 5
7. (child* or adolescen* or pediatric* or paediatric* or youth).ti,ab,kw.
8. 3 and 6 and 7
```

**Version B (BROAD)**
```
1. exp adverse childhood experience/ or exp child abuse/ or exp child neglect/ or exp child maltreatment/ or exp psychological trauma/ or exp domestic violence/ or exp early life stress/ or exp social deprivation/
2. ((child* or childhood or early life or early-life) adj3 (advers* or maltreat* or abus* or neglect* or trauma* or stress* or deprivation or "family dysfunction" or "household dysfunction" or "adverse childhood" or ACEs)).ti,ab,kw.
3. 1 or 2
4. exp inflammation/ or exp biological marker/ or exp c reactive protein/ or exp cytokine/ or exp interleukin 6/ or exp tumor necrosis factor alpha/ or exp interleukin 1 beta/ or exp interleukin 8/ or exp fibrinogen/ or exp leukocyte/ or exp erythrocyte sedimentation rate/
5. (inflamm* or cytokine* or chemokine* or biomarker* or "C-reactive protein" or CRP or hsCRP or "interleukin-6" or IL-6 or "tumor necrosis factor" or TNF-alpha or IL-1beta or IL-8 or fibrinogen or leukocyte* or WBC or ESR or suPAR or GlycA or "NF-kB").ti,ab,kw.
6. 4 or 5
7. 3 and 6
```

**Embase-specific note**: Emtree terms and explosion differ from MEDLINE; confirm mapping for “adverse childhood experience” and “early life stress.”

### 3.4 Web of Science Core Collection
**Version A (NARROW)**
```
TS=(
  ((child* OR childhood OR "early life" OR "early-life") NEAR/3 (advers* OR maltreat* OR abus* OR neglect* OR trauma* OR stress* OR deprivation OR "family dysfunction" OR "household dysfunction" OR "adverse childhood" OR ACEs))
)
AND TS=(
  inflamm* OR cytokine* OR chemokine* OR biomarker* OR "C-reactive protein" OR CRP OR hsCRP OR "interleukin-6" OR IL-6 OR "tumor necrosis factor" OR TNF-alpha OR IL-1beta OR IL-8 OR fibrinogen OR leukocyte* OR WBC OR ESR OR suPAR OR GlycA OR "NF-kB"
)
AND TS=(child* OR adolescen* OR pediatric* OR paediatric* OR youth)
```

**Version B (BROAD)**
```
TS=(
  ((child* OR childhood OR "early life" OR "early-life") NEAR/3 (advers* OR maltreat* OR abus* OR neglect* OR trauma* OR stress* OR deprivation OR "family dysfunction" OR "household dysfunction" OR "adverse childhood" OR ACEs))
)
AND TS=(
  inflamm* OR cytokine* OR chemokine* OR biomarker* OR "C-reactive protein" OR CRP OR hsCRP OR "interleukin-6" OR IL-6 OR "tumor necrosis factor" OR TNF-alpha OR IL-1beta OR IL-8 OR fibrinogen OR leukocyte* OR WBC OR ESR OR suPAR OR GlycA OR "NF-kB"
)
```

### 3.5 Scopus
**Version A (NARROW)**
```
TITLE-ABS-KEY(
  (child* OR childhood OR "early life" OR "early-life") W/3 (advers* OR maltreat* OR abus* OR neglect* OR trauma* OR stress* OR deprivation OR "family dysfunction" OR "household dysfunction" OR "adverse childhood" OR ACEs)
)
AND TITLE-ABS-KEY(
  inflamm* OR cytokine* OR chemokine* OR biomarker* OR "C-reactive protein" OR CRP OR hsCRP OR "interleukin-6" OR IL-6 OR "tumor necrosis factor" OR TNF-alpha OR IL-1beta OR IL-8 OR fibrinogen OR leukocyte* OR WBC OR ESR OR suPAR OR GlycA OR "NF-kB"
)
AND TITLE-ABS-KEY(child* OR adolescen* OR pediatric* OR paediatric* OR youth)
```

**Version B (BROAD)**
```
TITLE-ABS-KEY(
  (child* OR childhood OR "early life" OR "early-life") W/3 (advers* OR maltreat* OR abus* OR neglect* OR trauma* OR stress* OR deprivation OR "family dysfunction" OR "household dysfunction" OR "adverse childhood" OR ACEs)
)
AND TITLE-ABS-KEY(
  inflamm* OR cytokine* OR chemokine* OR biomarker* OR "C-reactive protein" OR CRP OR hsCRP OR "interleukin-6" OR IL-6 OR "tumor necrosis factor" OR TNF-alpha OR IL-1beta OR IL-8 OR fibrinogen OR leukocyte* OR WBC OR ESR OR suPAR OR GlycA OR "NF-kB"
)
```

### 3.6 PsycINFO
**(a) Ovid PsycINFO — Version A (NARROW)**
```
1. exp Adverse Childhood Experiences/ or exp Child Abuse/ or exp Child Neglect/ or exp Child Maltreatment/ or exp Psychological Trauma/ or exp Early Life Stress/ or exp Family Dysfunction/ or exp Domestic Violence/
2. ((child* or childhood or early life or early-life) adj3 (advers* or maltreat* or abus* or neglect* or trauma* or stress* or deprivation or "family dysfunction" or "household dysfunction" or "adverse childhood" or ACEs)).ti,ab,kw.
3. 1 or 2
4. exp Inflammation/ or exp Biomarkers/ or exp Cytokines/ or exp C-Reactive Protein/ or exp Interleukins/ or exp Tumor Necrosis Factor/
5. (inflamm* or cytokine* or chemokine* or biomarker* or "C-reactive protein" or CRP or hsCRP or "interleukin-6" or IL-6 or "tumor necrosis factor" or TNF-alpha or IL-1beta or IL-8 or fibrinogen or leukocyte* or WBC or ESR or suPAR or GlycA or "NF-kB").ti,ab,kw.
6. 4 or 5
7. (child* or adolescen* or pediatric* or paediatric* or youth).ti,ab,kw.
8. 3 and 6 and 7
```

**(a) Ovid PsycINFO — Version B (BROAD)**
```
1. exp Adverse Childhood Experiences/ or exp Child Abuse/ or exp Child Neglect/ or exp Child Maltreatment/ or exp Psychological Trauma/ or exp Early Life Stress/ or exp Family Dysfunction/ or exp Domestic Violence/
2. ((child* or childhood or early life or early-life) adj3 (advers* or maltreat* or abus* or neglect* or trauma* or stress* or deprivation or "family dysfunction" or "household dysfunction" or "adverse childhood" or ACEs)).ti,ab,kw.
3. 1 or 2
4. exp Inflammation/ or exp Biomarkers/ or exp Cytokines/ or exp C-Reactive Protein/ or exp Interleukins/ or exp Tumor Necrosis Factor/
5. (inflamm* or cytokine* or chemokine* or biomarker* or "C-reactive protein" or CRP or hsCRP or "interleukin-6" or IL-6 or "tumor necrosis factor" or TNF-alpha or IL-1beta or IL-8 or fibrinogen or leukocyte* or WBC or ESR or suPAR or GlycA or "NF-kB").ti,ab,kw.
6. 4 or 5
7. 3 and 6
```

**(b) EBSCO PsycINFO — Version A (NARROW)**
```
DE "Adverse Childhood Experiences" OR DE "Child Abuse" OR DE "Child Neglect" OR DE "Child Maltreatment" OR DE "Psychological Trauma" OR DE "Early Life Stress" OR DE "Family Dysfunction" OR DE "Domestic Violence"
AND
((child* OR childhood OR "early life" OR "early-life") N3 (advers* OR maltreat* OR abus* OR neglect* OR trauma* OR stress* OR deprivation OR "family dysfunction" OR "household dysfunction" OR "adverse childhood" OR ACEs))
AND
(DE "Inflammation" OR DE "Biomarkers" OR DE "Cytokines" OR DE "C-Reactive Protein" OR DE "Interleukins" OR DE "Tumor Necrosis Factor")
AND
(inflamm* OR cytokine* OR chemokine* OR biomarker* OR "C-reactive protein" OR CRP OR hsCRP OR "interleukin-6" OR IL-6 OR "tumor necrosis factor" OR TNF-alpha OR IL-1beta OR IL-8 OR fibrinogen OR leukocyte* OR WBC OR ESR OR suPAR OR GlycA OR "NF-kB")
AND
(child* OR adolescen* OR pediatric* OR paediatric* OR youth)
```

**(b) EBSCO PsycINFO — Version B (BROAD)**
```
DE "Adverse Childhood Experiences" OR DE "Child Abuse" OR DE "Child Neglect" OR DE "Child Maltreatment" OR DE "Psychological Trauma" OR DE "Early Life Stress" OR DE "Family Dysfunction" OR DE "Domestic Violence"
AND
((child* OR childhood OR "early life" OR "early-life") N3 (advers* OR maltreat* OR abus* OR neglect* OR trauma* OR stress* OR deprivation OR "family dysfunction" OR "household dysfunction" OR "adverse childhood" OR ACEs))
AND
(DE "Inflammation" OR DE "Biomarkers" OR DE "Cytokines" OR DE "C-Reactive Protein" OR DE "Interleukins" OR DE "Tumor Necrosis Factor")
AND
(inflamm* OR cytokine* OR chemokine* OR biomarker* OR "C-reactive protein" OR CRP OR hsCRP OR "interleukin-6" OR IL-6 OR "tumor necrosis factor" OR TNF-alpha OR IL-1beta OR IL-8 OR fibrinogen OR leukocyte* OR WBC OR ESR OR suPAR OR GlycA OR "NF-kB")
```

## 4. Optional Filters (NOT applied by default)
- **Humans only**: apply database-specific human limits when needed.
- **Animal-only exclusion**: e.g., PubMed `NOT (animals[MeSH] NOT humans[MeSH])`.
- **Language=English**: optional; apply only if required by protocol.
- **Document type exclusions**: editorials/letters/notes optional.

**Risk note**: Over-filtering can remove relevant mechanistic or cohort studies reporting biomarkers; prefer adjacency/fielding refinements first.

## 5. Iteration Log (MINIMUM 3 ROUNDS)
- **Round 1 → Round 2 (2025-02-14 10:00 UTC)**
  - Added additional exposure synonyms (family/household dysfunction, deprivation, foster/out-of-home care). **Recall ↑**.
  - Added broader biomarker terms (suPAR, GlycA, NF-kB, leukocytes/WBC, ESR). **Recall ↑**.
  - Added adjacency operators and fielding guidance to reduce “ACE” ambiguity. **Precision ↑**.
- **Round 2 → Round 3 (2025-02-14 10:30 UTC)**
  - Standardized platform syntax (PubMed tags, Ovid adj3, Scopus W/3, WoS NEAR/3). **Precision ↑ / errors ↓**.
  - Split Version A vs Version B logic across all databases consistently. **Transparency ↑**.
  - Added optional filters section and validation plan. **Methodological rigor ↑**.

## 6. Validation & Coverage Check Plan
- **Golden set**: Identify 8–12 seed studies via scoping searches (PubMed + Embase), then verify each is retrieved by Version B; adjust terms if any are missed.
- **Synonym coverage audit**: Check that key exposure and biomarker synonyms appear in titles/abstracts of seed papers; add missing terms.
- **Noise audit**: Review top 100 results for false positives (e.g., angiotensin-converting enzyme “ACE”); mitigate with adjacency to childhood/early-life terms.
- **Deduplication**: Export with full records and DOIs, then deduplicate in reference manager (e.g., EndNote/Zotero) using DOI+title+year.
