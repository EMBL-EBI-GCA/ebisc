from django.utils.translation import ugettext_lazy as _

from grappelli.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):

    def init_with_context(self, context):

        # User & groups
        self.children.append(modules.ModelList(
            _('Administration'),
            column=1,
            collapsible=False,
            models=('django.contrib.*',),
        ))

        self.children.append(modules.Group(
            _('EBiSC'),
            column=1,
            collapsible=False,
            children=[
                modules.ModelList(
                    _('Cell lines'),
                    collapsible=True,
                    column=1,
                    css_classes=('collapse closed',),
                    models=('ebisc.celllines.models.Aliquotstatus', 'ebisc.celllines.models.Batchstatus', 'ebisc.celllines.models.Binnedage', 'ebisc.celllines.models.Cellline', 'ebisc.celllines.models.Celllinecollection', 'ebisc.celllines.models.Celllinebatch', 'ebisc.celllines.models.Celllinealiquot', 'ebisc.celllines.models.Celllinechecklist', 'ebisc.celllines.models.Celltype', 'ebisc.celllines.models.Clinicaltreatmentb4donation', 'ebisc.celllines.models.Disease', 'ebisc.celllines.models.Donor', 'ebisc.celllines.models.Gender', 'ebisc.celllines.models.Phenotype', 'ebisc.celllines.models.Tissuesource',),
                ),
                modules.ModelList(
                    _('Lab, Derivation, Culture Conditions, Characterization, Karyotype'),
                    collapsible=True,
                    column=1,
                    css_classes=('collapse closed',),
                    models=('ebisc.celllines.models.Celllinecharacterization', 'ebisc.celllines.models.Celllinecultureconditions', 'ebisc.celllines.models.Celllineculturesupplements', 'ebisc.celllines.models.Celllinederivation', 'ebisc.celllines.models.Celllinekaryotype', 'ebisc.celllines.models.Celllinelab', 'ebisc.celllines.models.Culturemedium', 'ebisc.celllines.models.Culturesystem', 'ebisc.celllines.models.Enzymatically', 'ebisc.celllines.models.Enzymefree', 'ebisc.celllines.models.Karyotypemethod', 'ebisc.celllines.models.Reprogrammingmethod1', 'ebisc.celllines.models.Reprogrammingmethod2', 'ebisc.celllines.models.Reprogrammingmethod3', 'ebisc.celllines.models.Passagemethod', 'ebisc.celllines.models.Proteinsource', 'ebisc.celllines.models.Surfacecoating', 'ebisc.celllines.models.Units',),
                ),
                modules.ModelList(
                    _('Marker, Derivation, Differentiation Potency, Vectors'),
                    collapsible=True,
                    column=1,
                    css_classes=('collapse closed',),
                    models=('ebisc.celllines.models.Celllinederivation', 'ebisc.celllines.models.Celllinediffpotency', 'ebisc.celllines.models.Celllinediffpotencymarker', 'ebisc.celllines.models.Celllinediffpotencymolecule', 'ebisc.celllines.models.Celllinemarker', 'ebisc.celllines.models.Celllinevector', 'ebisc.celllines.models.Celllinevectormolecule', 'ebisc.celllines.models.Celllinevectorfreereprogramming', 'ebisc.celllines.models.Germlayer', 'ebisc.celllines.models.Marker', 'ebisc.celllines.models.Molecule', 'ebisc.celllines.models.Morphologymethod', 'ebisc.celllines.models.Primarycelldevelopmentalstage', 'ebisc.celllines.models.Transposon', 'ebisc.celllines.models.Vector', 'ebisc.celllines.models.Vectorfreereprogramfactor', 'ebisc.celllines.models.Vectortype', 'ebisc.celllines.models.Virus',),
                ),
                modules.ModelList(
                    _('Genotyping'),
                    collapsible=True,
                    column=1,
                    css_classes=('collapse closed',),
                    models=('ebisc.celllines.models.Celllinekaryotype', 'ebisc.celllines.models.Celllinegenemutations', 'ebisc.celllines.models.Celllinegenemutationsmolecule', 'ebisc.celllines.models.Celllinegeneticmod', 'ebisc.celllines.models.Celllinegenomeseq', 'ebisc.celllines.models.Celllinegenotypingother', 'ebisc.celllines.models.Celllinehlatyping', 'ebisc.celllines.models.Celllinemarker', 'ebisc.celllines.models.Celllinesnp', 'ebisc.celllines.models.Celllinesnpdetails', 'ebisc.celllines.models.Celllinesnprslinks', 'ebisc.celllines.models.Celllinestrfingerprinting', 'ebisc.celllines.models.Hla', 'ebisc.celllines.models.Molecule', 'ebisc.celllines.models.Strfplocus',),
                ),
                modules.ModelList(
                    _('Legal, Ethics, Documents, Publications'),
                    collapsible=True,
                    column=1,
                    css_classes=('collapse closed',),
                    models=('ebisc.celllines.models.Approveduse', 'ebisc.celllines.models.Celllineannotation', 'ebisc.celllines.models.Celllinecomments', 'ebisc.celllines.models.Celllinelegal', 'ebisc.celllines.models.Celllinepublication', 'ebisc.celllines.models.Celllinestatus', 'ebisc.celllines.models.Celllinevalue', 'ebisc.celllines.models.Document', 'ebisc.celllines.models.Documenttype', 'ebisc.celllines.models.Ebisckeyword', 'ebisc.celllines.models.Keyword', 'ebisc.celllines.models.Publisher',),
                ),
                modules.ModelList(
                    _('User Accounts, Organisations, Contacts'),
                    collapsible=True,
                    column=1,
                    css_classes=('collapse closed',),
                    models=('ebisc.celllines.models.Accesslevel', 'ebisc.celllines.models.Celllineorganization', 'ebisc.celllines.models.Celllineorgtype', 'ebisc.celllines.models.Contact', 'ebisc.celllines.models.Contacttype', 'ebisc.celllines.models.Country', 'ebisc.celllines.models.Lastupdatetype', 'ebisc.celllines.models.Organization', 'ebisc.celllines.models.Orgtype', 'ebisc.celllines.models.Person', 'ebisc.celllines.models.Phonecountrycode', 'ebisc.celllines.models.Postcode', 'ebisc.celllines.models.Useraccount', 'ebisc.celllines.models.Useraccounttype',),
                ),
            ]
        ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Links'),
            column=2,
            collapsible=False,
            children=[
                {
                    'title': _('EBiSC Home'),
                    'url': 'http://www.ebisc.org/',
                    'external': True,
                },
                {
                    'title': _('hESCreg'),
                    'url': 'http://www.hescreg.eu/',
                    'external': True,
                },
            ]
        ))

'''

View 1 / Cell line

'ebisc.celllines.models.Aliquotstatus', 'ebisc.celllines.models.Batchstatus', 'ebisc.celllines.models.Binnedage', 'ebisc.celllines.models.Cellline', 'ebisc.celllines.models.Celllinecollection', 'ebisc.celllines.models.Celllinebatch', 'ebisc.celllines.models.Celllinealiquot', 'ebisc.celllines.models.Celllinechecklist', 'ebisc.celllines.models.Celltype', 'ebisc.celllines.models.Clinicaltreatmentb4donation', 'ebisc.celllines.models.Disease', 'ebisc.celllines.models.Donor', 'ebisc.celllines.models.Gender', 'ebisc.celllines.models.Phenotype', 'ebisc.celllines.models.Tissuesource', 

View 2 / Lab, Derivation, Culture Conditions, Characterization, Karyotype

'ebisc.celllines.models.Celllinecharacterization', 'ebisc.celllines.models.Celllinecultureconditions', 'ebisc.celllines.models.Celllineculturesupplements', 'ebisc.celllines.models.Celllinederivation', 'ebisc.celllines.models.Celllinekaryotype', 'ebisc.celllines.models.Celllinelab', 'ebisc.celllines.models.Culturemedium', 'ebisc.celllines.models.Culturesystem', 'ebisc.celllines.models.Enzymatically', 'ebisc.celllines.models.Enzymefree', 'ebisc.celllines.models.Karyotypemethod', 'ebisc.celllines.models.Reprogrammingmethod1', 'ebisc.celllines.models.Reprogrammingmethod2', 'ebisc.celllines.models.Reprogrammingmethod3', 'ebisc.celllines.models.Passagemethod', 'ebisc.celllines.models.Proteinsource', 'ebisc.celllines.models.Surfacecoating', 'ebisc.celllines.models.Units', 

View 3 / Marker, Derivation, Differentiation Potency, Vector

'ebisc.celllines.models.Celllinederivation', 'ebisc.celllines.models.Celllinediffpotency', 'ebisc.celllines.models.Celllinediffpotencymarker', 'ebisc.celllines.models.Celllinediffpotencymolecule', 'ebisc.celllines.models.Celllinemarker', 'ebisc.celllines.models.Celllinevector', 'ebisc.celllines.models.Celllinevectormolecule', 'ebisc.celllines.models.Celllinevectorfreereprogramming', 'ebisc.celllines.models.Germlayer', 'ebisc.celllines.models.Marker', 'ebisc.celllines.models.Molecule', 'ebisc.celllines.models.Morphologymethod', 'ebisc.celllines.models.Primarycelldevelopmentalstage', 'ebisc.celllines.models.Transposon', 'ebisc.celllines.models.Vector', 'ebisc.celllines.models.Vectorfreereprogramfactor', 'ebisc.celllines.models.Vectortype', 'ebisc.celllines.models.Virus', 

View 4 / Genotyping

'ebisc.celllines.models.Celllinekaryotype', 'ebisc.celllines.models.Celllinegenemutations', 'ebisc.celllines.models.Celllinegenemutationsmolecule', 'ebisc.celllines.models.Celllinegeneticmod', 'ebisc.celllines.models.Celllinegenomeseq', 'ebisc.celllines.models.Celllinegenotypingother', 'ebisc.celllines.models.Celllinehlatyping', 'ebisc.celllines.models.Celllinemarker', 'ebisc.celllines.models.Celllinesnp', 'ebisc.celllines.models.Celllinesnpdetails', 'ebisc.celllines.models.Celllinesnprslinks', 'ebisc.celllines.models.Celllinestrfingerprinting', 'ebisc.celllines.models.Hla', 'ebisc.celllines.models.Molecule', 'ebisc.celllines.models.Strfplocus', 

View 5 / Legal, Ethics, Documents, publications

'ebisc.celllines.models.Approveduse', 'ebisc.celllines.models.Celllineannotation', 'ebisc.celllines.models.Celllinecomments', 'ebisc.celllines.models.Celllinelegal', 'ebisc.celllines.models.Celllinepublication', 'ebisc.celllines.models.Celllinestatus', 'ebisc.celllines.models.Celllinevalue', 'ebisc.celllines.models.Document', 'ebisc.celllines.models.Documenttype', 'ebisc.celllines.models.Ebisckeyword', 'ebisc.celllines.models.Keyword', 'ebisc.celllines.models.Publisher', 

View 6 / Accounts, Organisations, contacts

'ebisc.celllines.models.Accesslevel', 'ebisc.celllines.models.Celllineorganization', 'ebisc.celllines.models.Celllineorgtype', 'ebisc.celllines.models.Contact', 'ebisc.celllines.models.Contacttype', 'ebisc.celllines.models.Country', 'ebisc.celllines.models.Lastupdatetype', 'ebisc.celllines.models.Organization', 'ebisc.celllines.models.Orgtype', 'ebisc.celllines.models.Person', 'ebisc.celllines.models.Phonecountrycode', 'ebisc.celllines.models.Postcode', 'ebisc.celllines.models.Useraccount', 'ebisc.celllines.models.Useraccounttype', 







------
Accesslevel
Aliquotstatus
Approveduse
Batchstatus
Binnedage
Cellline
Celllinealiquot
Celllineannotation
Celllinebatch
Celllinecharacterization
Celllinechecklist
Celllinecollection
Celllinecomments
Celllinecultureconditions
Celllineculturesupplements
Celllinederivation
Celllinediffpotency
Celllinediffpotencymarker
Celllinediffpotencymolecule
Celllinegenemutations
Celllinegenemutationsmolecule
Celllinegeneticmod
Celllinegenomeseq
Celllinegenotypingother
Celllinehlatyping
Celllinekaryotype
Celllinelab
Celllinelegal
Celllinemarker
Celllineorganization
Celllineorgtype
Celllinepublication
Celllinesnp
Celllinesnpdetails
Celllinesnprslinks
Celllinestatus
Celllinestrfingerprinting
Celllinevalue
Celllinevector
Celllinevectorfreereprogramming
Celllinevectormolecule
Celltype
Clinicaltreatmentb4donation
Contact
Contacttype
Country
Culturemedium
Culturesystem
Disease
Document
Documenttype
Donor
Ebisckeyword
Enzymatically
Enzymefree
Gender
Germlayer
Hla
Karyotypemethod
Keyword
Lastupdatetype
Marker
Molecule
Morphologymethod
Organization
Orgtype
Passagemethod
Person
Phenotype
Phonecountrycode
Postcode
Primarycelldevelopmentalstage
Proteinsource
Publisher
Reprogrammingmethod1
Reprogrammingmethod2
Reprogrammingmethod3
Strfplocus
Surfacecoating
Tissuesource
Transposon
Units
Useraccount
Useraccounttype
Vector
Vectorfreereprogramfactor
Vectortype
Virus
'''
