#pragma once

// system include files
#include <memory>
#include <vector>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "TFile.h"
#include "TTree.h"

class genTuple : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit genTuple(const edm::ParameterSet&);
      ~genTuple();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
      void fillTTree();

      // ----------member data ---------------------------
      edm::EDGetTokenT<reco::GenParticleCollection> genParticleToken_;  //used to select what tracks to read from configuration file
      edm::EDGetTokenT<GenEventInfoProduct> GenEventToken_;
      TTree* tree_;

      std::vector<float> *gen_pt, *gen_eta, *gen_phi, *gen_mass, *gen_vx, *gen_vy, *gen_vz;
      std::vector<int> *gen_pdgId, *gen_status, *gen_ndaughters, *gen_charge, *gen_genPartIdxMother;
      unsigned int nGen;
      unsigned int run, event, luminosityBlock;
      float ptHat, qScale;

      std::vector<int> savePdgId;
      bool saveAll;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//
