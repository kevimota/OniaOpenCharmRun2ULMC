// -*- C++ -*-
//
// Package:    genTuple/genTuple
// Class:      genTuple
//
/**\class genTuple genTuple.cc genTuple/genTuple/plugins/genTuple.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Kevin Mota Amarilo
//         Created:  Thu, 25 Nov 2021 10:24:16 GMT
//
//

#include "genTuple.h"

genTuple::genTuple(const edm::ParameterSet& iConfig)
 :
  genParticleToken_(consumes<reco::GenParticleCollection>(edm::InputTag("genParticles"))),
  GenEventToken_(consumes<GenEventInfoProduct>(edm::InputTag("generator"))),
  tree_(0),
  gen_pt(0), gen_eta(0), gen_phi(0), gen_mass(0), gen_vx(0), gen_vy(0), gen_vz(0),
  gen_pdgId(0), gen_status(0), gen_ndaughters(0), gen_charge(0), gen_genPartIdxMother(0),
  nGen(0),
  run(0), event(0), luminosityBlock(0)

{
   std::vector<int> defsavePdgId;
   defsavePdgId.push_back(0);
   bool defsaveAll = false;
   savePdgId = iConfig.getUntrackedParameter<std::vector<int>>("savePdgId", defsavePdgId);
   saveAll = iConfig.getUntrackedParameter<bool>("saveAll", defsaveAll);
}


genTuple::~genTuple()
{
}


//
// member functions
//

// ------------ method called for each event  ------------
void
genTuple::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   edm::Handle<GenEventInfoProduct> GenInfoHandle;
   edm::Handle<reco::GenParticleCollection> genParticles;
   iEvent.getByToken(genParticleToken_, genParticles);
   iEvent.getByToken(GenEventToken_, GenInfoHandle);
   
   run = (iEvent.id()).run();
   event = (iEvent.id()).event();
   luminosityBlock = (iEvent.id()).luminosityBlock();

   qScale = GenInfoHandle->qScale();
   ptHat = (GenInfoHandle->hasBinningValues() ? (GenInfoHandle->binningValues())[0] : 0.0);
   
   for(const auto& genParticle : *genParticles) {
      bool save = false;
      if (saveAll) {
         save = true;
      }
      else {
         for (const auto &id : savePdgId) {
            if (genParticle.pdgId() == id) {
               save = true;
            }
         }
      }   
      if (!save) continue;

      gen_pt->push_back(genParticle.pt());
      gen_eta->push_back(genParticle.eta());
      gen_phi->push_back(genParticle.phi());
      gen_mass->push_back(genParticle.mass()); 
      gen_vx->push_back(genParticle.vx()); 
      gen_vy->push_back(genParticle.vy()); 
      gen_vz->push_back(genParticle.vz());
      gen_pdgId->push_back(genParticle.pdgId()); 
      gen_status->push_back(genParticle.status()); 
      gen_ndaughters->push_back(genParticle.numberOfDaughters()); 
      gen_charge->push_back(genParticle.charge());

      const reco::Candidate *mom = genParticle.mother();


      int m_idx = -99;
      for (unsigned int i = 0; i < gen_pt->size(); ++i) {
         if (mom == nullptr) continue;
         if ((mom->pt() == gen_pt->at(i)) & (mom->eta() == gen_eta->at(i))) {
            m_idx = (int) i;
         }
      }
      
      gen_genPartIdxMother->push_back(m_idx);

      ++nGen;
   }

   fillTTree();
}

void genTuple::fillTTree()
{
   if (nGen > 0 ) {
      tree_->Fill();
   }
   nGen = 0;
   gen_pt->clear();
   gen_eta->clear();
   gen_phi->clear();
   gen_mass->clear();
   gen_vx->clear();
   gen_vy->clear();
   gen_vz->clear();
   gen_pdgId->clear();
   gen_status->clear();
   gen_ndaughters->clear();
   gen_charge->clear();
   gen_genPartIdxMother->clear();
   run = 0;
   event = 0;
   luminosityBlock = 0;
   ptHat = 0;
   qScale = 0;
}

// ------------ method called once each job just before starting event loop  ------------
void
genTuple::beginJob()
{
   edm::Service<TFileService> fs;
   tree_ = fs->make<TTree>("Events","Dump of GenParticle");

   tree_->Branch("GenPart_pt", &gen_pt);
   tree_->Branch("GenPart_eta", &gen_eta);
   tree_->Branch("GenPart_phi", &gen_phi);
   tree_->Branch("GenPart_mass", &gen_mass);
   tree_->Branch("GenPart_vx", &gen_vx);
   tree_->Branch("GenPart_vy", &gen_vy);
   tree_->Branch("GenPart_vz", &gen_vz);
   tree_->Branch("GenPart_pdgId", &gen_pdgId);
   tree_->Branch("GenPart_status", &gen_status);
   tree_->Branch("GenPart_numberOfDaughters", &gen_ndaughters);
   tree_->Branch("GenPart_charge", &gen_charge);
   tree_->Branch("GenPart_genPartIdxMother", &gen_genPartIdxMother);
   tree_->Branch("Info_run", &run);
   tree_->Branch("Info_event", &event);
   tree_->Branch("Info_luminosityBlock", &luminosityBlock);
   tree_->Branch("Info_ptHat", &ptHat);
   tree_->Branch("Info_qScale", &qScale);
}

// ------------ method called once each job just after ending the event loop  ------------
void
genTuple::endJob()
{
   tree_->GetDirectory()->cd();
   tree_->Write();
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
genTuple::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  std::vector<int> defsavePdgId;
  defsavePdgId.push_back(0);
  bool defsaveAll = false;
  edm::ParameterSetDescription desc;
  desc.addUntracked<std::vector<int>>("savePdgId", defsavePdgId);
  desc.addUntracked<bool>("saveAll", defsaveAll);
  descriptions.addDefault(desc);

  //Specify that only 'tracks' is allowed
  //To use, remove the default given above and uncomment below
  //ParameterSetDescription desc;
  //desc.addUntracked<edm::InputTag>("tracks","ctfWithMaterialTracks");
  //descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(genTuple);
