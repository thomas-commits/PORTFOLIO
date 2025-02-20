def print_final_populations():
    """Print the final populations stored in results_aggregator in a structured format."""
    final_populations = results_aggregator.get_final_populations()

    if not final_populations:
        print("\n🚨 No final populations stored! Run the genetic algorithm first.")
        return

    print("\n" + "=" * 50)
    print(" 📌 FINAL POPULATIONS REPORT ")
    print("=" * 50)

    for pop_size, gens, population in final_populations:
        print(f"\n🔹 Population Size: {pop_size} | Generations: {gens}")
        print("-" * 50)
        
        if not population:
            print("   ⚠️ No individuals in this population.")
            continue

        print(f"   {'Chromosome':<25} | Fitness")
        print("   " + "-" * 40)

        for chromosome, fitness in population:
            chromosome_str = " ".join(map(str, chromosome))  # Format chromosome nicely
            print(f"   {chromosome_str:<25} | {fitness:.2f}")

        print("-" * 50)

    print("\n✅ End of Report")
    print("=" * 50)

# Run only when executed as a script
if __name__ == "__main__":
    print_final_populations()
